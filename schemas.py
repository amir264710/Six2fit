from pydantic import BaseModel
from typing import Optional

class ClientCreate(BaseModel):
    first_name: str
    last_name: str
    current_weight_kg: float
    height_cm: float
    gender: int
    age: int
    activity_level: Optional[int] = None
    body_fat_percentage: Optional[float] = None
    last_program_id: Optional[int] = None
    meal_preference: int = 0
    food_allergies: Optional[str] = None
    disliked_foods: Optional[str] = None
    special_conditions: Optional[str] = None

class PlanCreate(BaseModel):
    client_id: int
    duration: Optional[int] = None
    current_weight: Optional[int] = None
    goal_weight: Optional[int] = None
    type_of_plan: Optional[int] = None
    create_date: Optional[str] = None  # Expected in "YYYY-MM-DD" format
    target_calorie_pr: Optional[int] = None
    meal_frequency: Optional[int] = None
    meal_preference: Optional[str] = None
    meal_avoids: Optional[str] = None
    special_cases: Optional[str] = None
    preferred_kind_food: Optional[str] = None
    access_to_cooking: Optional[int] = None
    plan_file_path: Optional[str] = None
    plan_rarity: Optional[int] = None
