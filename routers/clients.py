from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas, crud
from database import get_db

router = APIRouter()

@router.post("/clients/")
def add_client(
    first_name: str,
    last_name: str,
    current_weight_kg: float,
    height_cm: float,
    gender: int,
    age: int,
    activity_level: int = None,
    body_fat_percentage: float = None,
    last_program_id: int = None,
    meal_preference: int = 0,
    food_allergies: str = None,
    disliked_foods: str = None,
    special_conditions: str = None,
    db: Session = Depends(get_db)
):
    client_data = schemas.ClientCreate(
        first_name=first_name,
        last_name=last_name,
        current_weight_kg=current_weight_kg,
        height_cm=height_cm,
        gender=gender,
        age=age,
        activity_level=activity_level,
        body_fat_percentage=body_fat_percentage,
        last_program_id=last_program_id,
        meal_preference=meal_preference,
        food_allergies=food_allergies,
        disliked_foods=disliked_foods,
        special_conditions=special_conditions
    )
    return crud.create_client(db=db, client=client_data)
