# Lock_In

Lock_In is a starter project for a dieting AI assistant. This version includes:

- A local Python web server with a JSON API
- A browser-based intake form for generating a meal plan
- A rules-based planner that can later be swapped for an LLM-backed planner
- A clean project structure for future nutrition, user-profile, and OpenAI work

## Project Structure

```text
Lock_In/
├── app.py
├── lock_in/
│   ├── __init__.py
│   ├── models.py
│   ├── openai_client.py
│   ├── planner.py
│   └── server.py
├── static/
│   └── index.html
├── tests/
│   └── test_planner.py
├── Phase One/
│   ├── Phase 1 Doc
│   └── Presentation
└── Phase 3/
    └── Phase 3 Doc
```

## Run Locally

1. Open a terminal.
2. Change into the repo:

```bash
cd /Users/ryancraft/Documents/Lock_In
```

3. Start the server:

```bash
python3 app.py
```

4. Open your browser to:

```text
http://127.0.0.1:8000
```

## Run Tests

```bash
cd /Users/ryancraft/Documents/Lock_In
python3 -m unittest discover -s tests -v
```

## API Endpoints

- `GET /api/health` returns a simple health payload
- `POST /api/plan` generates a dieting-focused meal plan

Example request body:

```json
{
  "name": "Ryan",
  "age": 21,
  "height_cm": 178,
  "weight_kg": 84,
  "activity_level": "moderate",
  "goal": "fat_loss",
  "diet_style": "high_protein",
  "meals_per_day": 4,
  "allergies": ["peanuts"],
  "dislikes": ["tuna"]
}
```

## Where To Build The Dieting AI Next

The most important files for the actual dieting AI are:

- `lock_in/planner.py`: main meal-plan generation logic
- `lock_in/models.py`: input and output data structures
- `lock_in/openai_client.py`: placeholder for future OpenAI integration
- `lock_in/server.py`: API routes and request handling
- `static/index.html`: prototype frontend for testing user flows

## Existing Project Docs

The original course/project artifacts are still here:

- `Phase One/Phase 1 Doc`
- `Phase One/Presentation`
- `Phase 3/Phase 3 Doc`

Those are useful for project planning, but the files listed above are now the main implementation surface.
