from __future__ import annotations

from dataclasses import asdict, dataclass, field


VALID_ACTIVITY_LEVELS = {"sedentary", "light", "moderate", "active"}
VALID_GOALS = {"fat_loss", "muscle_gain", "maintenance"}


@dataclass
class UserProfile:
    name: str
    age: int
    height_cm: float
    weight_kg: float
    activity_level: str
    goal: str
    diet_style: str
    meals_per_day: int
    allergies: list[str] = field(default_factory=list)
    dislikes: list[str] = field(default_factory=list)

    @classmethod
    def from_payload(cls, payload: dict) -> "UserProfile":
        required_fields = {
            "name",
            "age",
            "height_cm",
            "weight_kg",
            "activity_level",
            "goal",
            "diet_style",
            "meals_per_day",
        }
        missing = sorted(required_fields - payload.keys())
        if missing:
            raise ValueError(f"Missing required fields: {', '.join(missing)}")

        profile = cls(
            name=str(payload["name"]).strip(),
            age=int(payload["age"]),
            height_cm=float(payload["height_cm"]),
            weight_kg=float(payload["weight_kg"]),
            activity_level=str(payload["activity_level"]).strip().lower(),
            goal=str(payload["goal"]).strip().lower(),
            diet_style=str(payload["diet_style"]).strip().lower(),
            meals_per_day=int(payload["meals_per_day"]),
            allergies=_normalize_list(payload.get("allergies", [])),
            dislikes=_normalize_list(payload.get("dislikes", [])),
        )
        profile.validate()
        return profile

    def validate(self) -> None:
        if not self.name:
            raise ValueError("Name cannot be empty.")
        if self.age <= 0:
            raise ValueError("Age must be greater than 0.")
        if self.height_cm <= 0 or self.weight_kg <= 0:
            raise ValueError("Height and weight must be greater than 0.")
        if self.meals_per_day not in {3, 4, 5, 6}:
            raise ValueError("Meals per day must be one of 3, 4, 5, or 6.")
        if self.activity_level not in VALID_ACTIVITY_LEVELS:
            allowed = ", ".join(sorted(VALID_ACTIVITY_LEVELS))
            raise ValueError(f"Activity level must be one of: {allowed}")
        if self.goal not in VALID_GOALS:
            allowed = ", ".join(sorted(VALID_GOALS))
            raise ValueError(f"Goal must be one of: {allowed}")

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Meal:
    name: str
    calories: int
    protein_g: int
    carbs_g: int
    fats_g: int
    notes: str


@dataclass
class MealPlan:
    daily_calories: int
    protein_target_g: int
    carbs_target_g: int
    fats_target_g: int
    hydration_goal_liters: float
    rationale: str
    meals: list[Meal]

    def to_dict(self) -> dict:
        return {
            "daily_calories": self.daily_calories,
            "protein_target_g": self.protein_target_g,
            "carbs_target_g": self.carbs_target_g,
            "fats_target_g": self.fats_target_g,
            "hydration_goal_liters": self.hydration_goal_liters,
            "rationale": self.rationale,
            "meals": [asdict(meal) for meal in self.meals],
        }


def _normalize_list(value: object) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        items = value
    elif isinstance(value, str):
        items = value.split(",")
    else:
        raise ValueError("Expected a list or comma-separated string.")

    normalized = [str(item).strip().lower() for item in items if str(item).strip()]
    return normalized
