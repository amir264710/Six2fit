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
