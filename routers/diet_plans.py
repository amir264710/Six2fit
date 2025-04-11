from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas, crud
from database import get_db

router = APIRouter()

@router.post("/diet_plans/")
def add_diet_plan(
    client_id: int,
    duration: int = None,
    current_weight: int = None,
    goal_weight: int = None,
    type_of_plan: int = None,
    create_date: str = None,  # expected in "YYYY-MM-DD" format
    target_calorie_pr: int = None,
    meal_frequency: int = None,
    meal_preference: str = None,
    meal_avoids: str = None,
    special_cases: str = None,
    preferred_kind_food: str = None,
    access_to_cooking: int = None,
    plan_file_path: str = None,
    plan_rarity: int = None,
    db: Session = Depends(get_db)
):
    plan_data = schemas.PlanCreate(
        client_id=client_id,
        duration=duration,
        current_weight=current_weight,
        goal_weight=goal_weight,
        type_of_plan=type_of_plan,
        create_date=create_date,
        target_calorie_pr=target_calorie_pr,
        meal_frequency=meal_frequency,
        meal_preference=meal_preference,
        meal_avoids=meal_avoids,
        special_cases=special_cases,
        preferred_kind_food=preferred_kind_food,
        access_to_cooking=access_to_cooking,
        plan_file_path=plan_file_path,
        plan_rarity=plan_rarity
    )
    return crud.create_diet_plan(db=db, plan=plan_data)