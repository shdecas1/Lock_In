from __future__ import annotations

from lock_in.models import Meal, MealPlan, UserProfile


ACTIVITY_MULTIPLIERS = {
    "sedentary": 1.2,
    "light": 1.375,
    "moderate": 1.55,
    "active": 1.725,
}


MEAL_LIBRARY = {
    "breakfast": [
        ("Greek yogurt bowl", "Greek yogurt, berries, oats, chia seeds"),
        ("Protein oatmeal", "Oats with whey or soy protein and banana"),
        ("Egg scramble", "Eggs, spinach, potatoes, and fruit"),
    ],
    "lunch": [
        ("Chicken rice bowl", "Chicken breast, rice, vegetables, olive oil"),
        ("Turkey wrap", "Turkey, whole-grain wrap, hummus, greens"),
        ("Tofu grain bowl", "Tofu, quinoa, roasted vegetables"),
    ],
    "dinner": [
        ("Salmon plate", "Salmon, sweet potato, broccoli"),
        ("Lean beef bowl", "Lean beef, potatoes, salad"),
        ("Bean pasta dinner", "High-protein pasta, beans, tomato sauce"),
    ],
    "snack": [
        ("Protein shake", "Protein shake with fruit"),
        ("Cottage cheese cup", "Cottage cheese with pineapple"),
        ("Trail mix alternative", "Pumpkin seeds and dried fruit"),
    ],
}


def generate_meal_plan(profile: UserProfile) -> MealPlan:
    daily_calories = _estimate_daily_calories(profile)
    protein_target = round(profile.weight_kg * _protein_multiplier(profile.goal))
    fats_target = max(45, round(daily_calories * 0.25 / 9))
    carbs_target = max(100, round((daily_calories - protein_target * 4 - fats_target * 9) / 4))
    hydration_goal = round(max(2.0, profile.weight_kg * 0.035), 1)

    meals = _build_meals(profile, daily_calories, protein_target, carbs_target, fats_target)
    rationale = (
        f"This plan targets {daily_calories} kcal/day for {profile.goal.replace('_', ' ')} "
        f"with an emphasis on {profile.diet_style.replace('_', ' ')} eating."
    )

    return MealPlan(
        daily_calories=daily_calories,
        protein_target_g=protein_target,
        carbs_target_g=carbs_target,
        fats_target_g=fats_target,
        hydration_goal_liters=hydration_goal,
        rationale=rationale,
        meals=meals,
    )


def _estimate_daily_calories(profile: UserProfile) -> int:
    bmr = 10 * profile.weight_kg + 6.25 * profile.height_cm - 5 * profile.age + 5
    maintenance = bmr * ACTIVITY_MULTIPLIERS[profile.activity_level]

    if profile.goal == "fat_loss":
        maintenance -= 400
    elif profile.goal == "muscle_gain":
        maintenance += 250

    return max(1400, round(maintenance))


def _protein_multiplier(goal: str) -> float:
    if goal == "fat_loss":
        return 2.0
    if goal == "muscle_gain":
        return 2.2
    return 1.8


def _build_meals(
    profile: UserProfile,
    daily_calories: int,
    protein_target: int,
    carbs_target: int,
    fats_target: int,
) -> list[Meal]:
    meal_types = _meal_type_sequence(profile.meals_per_day)
    per_meal_calories = round(daily_calories / len(meal_types))
    per_meal_protein = round(protein_target / len(meal_types))
    per_meal_carbs = round(carbs_target / len(meal_types))
    per_meal_fats = round(fats_target / len(meal_types))

    meals: list[Meal] = []
    for index, meal_type in enumerate(meal_types):
        template = _select_template(profile, meal_type, index)
        meals.append(
            Meal(
                name=template[0],
                calories=per_meal_calories,
                protein_g=per_meal_protein,
                carbs_g=per_meal_carbs,
                fats_g=per_meal_fats,
                notes=_build_notes(profile, template[1]),
            )
        )
    return meals


def _meal_type_sequence(meals_per_day: int) -> list[str]:
    if meals_per_day == 3:
        return ["breakfast", "lunch", "dinner"]
    if meals_per_day == 4:
        return ["breakfast", "lunch", "snack", "dinner"]
    if meals_per_day == 5:
        return ["breakfast", "snack", "lunch", "snack", "dinner"]
    return ["breakfast", "snack", "lunch", "snack", "dinner", "snack"]


def _select_template(profile: UserProfile, meal_type: str, offset: int) -> tuple[str, str]:
    options = MEAL_LIBRARY[meal_type]
    filtered = [
        option
        for option in options
        if not any(dislike in option[0].lower() or dislike in option[1].lower() for dislike in profile.dislikes)
    ]
    chosen_pool = filtered or options
    return chosen_pool[offset % len(chosen_pool)]


def _build_notes(profile: UserProfile, base_description: str) -> str:
    notes = [base_description]
    if profile.allergies:
        notes.append(f"Avoid allergens: {', '.join(profile.allergies)}.")
    if profile.goal == "fat_loss":
        notes.append("Prioritize high-volume vegetables and lean protein.")
    elif profile.goal == "muscle_gain":
        notes.append("Include a carb source around training.")
    else:
        notes.append("Aim for consistency and sustainable portions.")
    return " ".join(notes)
