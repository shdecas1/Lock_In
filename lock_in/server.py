from __future__ import annotations

import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from lock_in.models import UserProfile
from lock_in.planner import generate_meal_plan


HOST = "127.0.0.1"
PORT = 8000
STATIC_DIR = Path(__file__).resolve().parent.parent / "static"


class LockInHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path in {"/", "/index.html"}:
            self._serve_index()
            return

        if self.path == "/api/health":
            self._send_json(HTTPStatus.OK, {"status": "ok", "service": "lock_in"})
            return

        self._send_json(HTTPStatus.NOT_FOUND, {"error": "Not found"})

    def do_POST(self) -> None:
        if self.path != "/api/plan":
            self._send_json(HTTPStatus.NOT_FOUND, {"error": "Not found"})
            return

        try:
            content_length = int(self.headers.get("Content-Length", "0"))
            raw_body = self.rfile.read(content_length)
            payload = json.loads(raw_body or b"{}")
            profile = UserProfile.from_payload(payload)
            plan = generate_meal_plan(profile)
        except json.JSONDecodeError:
            self._send_json(HTTPStatus.BAD_REQUEST, {"error": "Request body must be valid JSON."})
            return
        except ValueError as exc:
            self._send_json(HTTPStatus.BAD_REQUEST, {"error": str(exc)})
            return

        response = {"profile": profile.to_dict(), "plan": plan.to_dict()}
        self._send_json(HTTPStatus.OK, response)

    def log_message(self, format: str, *args) -> None:
        return

    def _serve_index(self) -> None:
        body = (STATIC_DIR / "index.html").read_bytes()
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_json(self, status: HTTPStatus, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def run() -> None:
    server = ThreadingHTTPServer((HOST, PORT), LockInHandler)
    print(f"Lock_In running at http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down Lock_In...")
    finally:
        server.server_close()
