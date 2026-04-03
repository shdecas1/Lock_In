import unittest

from lock_in.models import UserProfile
from lock_in.planner import generate_meal_plan


class PlannerTests(unittest.TestCase):
    def test_generates_expected_number_of_meals(self) -> None:
        profile = UserProfile.from_payload(
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
                "dislikes": ["tuna"],
            }
        )

        plan = generate_meal_plan(profile)

        self.assertEqual(len(plan.meals), 4)
        self.assertGreaterEqual(plan.daily_calories, 1400)
        self.assertIn("fat loss", plan.rationale)

    def test_rejects_invalid_activity_level(self) -> None:
        with self.assertRaises(ValueError):
            UserProfile.from_payload(
                {
                    "name": "Ryan",
                    "age": 21,
                    "height_cm": 178,
                    "weight_kg": 84,
                    "activity_level": "extreme",
                    "goal": "fat_loss",
                    "diet_style": "high_protein",
                    "meals_per_day": 4,
                }
            )


if __name__ == "__main__":
    unittest.main()
