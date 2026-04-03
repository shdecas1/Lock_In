from __future__ import annotations

import os

from lock_in.models import MealPlan, UserProfile


def openai_available() -> bool:
    return bool(os.getenv("OPENAI_API_KEY"))


def generate_ai_plan(profile: UserProfile) -> MealPlan:
    raise NotImplementedError(
        "OpenAI integration is not wired up yet. Use the rules-based planner for now, "
        "or replace this module with a real API client."
    )
