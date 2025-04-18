from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas, crud
from database import get_db
from openai import OpenAI
import os
from datetime import datetime

router = APIRouter()

client = OpenAI(api_key=os.getenv("API_KEY"))

def generate_html(question, client_id):
    response = client.chat.completions.create(
        model="o3-mini",
        messages=[
            {"role": "system", "content": "You are an expert nutritionist and web developer. Provide a well-structured HTML document based on the data provided."},
            {"role": "user", "content": question}
        ]
    )

    generated_html = response.choices[0].message.content

    # Create filename based on client id and current date
    current_date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    filename = f"/home/{client_id}_{current_date}.html"

    # Save the HTML response to the file
    with open(filename, "w", encoding="utf-8") as file:
        file.write(generated_html)

    return {"html": generated_html, "file_saved": filename}

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

@router.post("/generate/{client_id}")
def generate_diet_plan(
    client_id: int,
    plan: schemas.PlanCreate,
    db: Session = Depends(get_db)
):
    # Retrieve the client data from the database
    client = crud.get_client(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    
    # Convert numeric fields to text
    gender_text = "Male" if client.gender == 1 else "Female"

    activity_text = (
        "Sedentary" if client.activity_level == 1
        else "Light activity " if client.activity_level == 2
        else "Moderate activity" if client.activity_level == 3
        else "High activity" if client.activity_level == 4
        else "Professional athlete" if client.activity_level == 5
        else "Unknown"
    )

    preferred_kind_food = (
        "Common Iranian Meals" if plan.preferred_kind_food == 1
        else "General/International Meals" if plan.preferred_kind_food == 2
        else "No Specific Preference" if plan.preferred_kind_food == 3
        else "Unknown"
    )

    access_to_cooking_text= (
        "Low Access - Up to 30 minutes per day" if plan.access_to_cooking == 1
        else "Medium Access - 30 to 90 minutes per day" if plan.access_to_cooking == 2
        else "High Access - More than 90 minutes per day" if plan.access_to_cooking == 3
        else "Unknown (Assume around 15 minutes to 25 minutes per day)"
    )

    # Compose the complete question with instructions as an f-string
    question = f"""
Based on the info that the client has provided, create a diet plan for the customer.
The diet plan should be in HTML format and include the following sections and your response should be in 
HTML format whithout any other text or comments:
the clinet is a {client.age} old {gender_text}, who is {client.current_weight_kg} kg and {client.height_cm} cm tall
and wanted to be {plan.goal_weight} kg, so he needed to lose {client.current_weight_kg - plan.goal_weight} kg and have
average of {plan.target_calorie_pr} per day. 
The client is {activity_text} and can spend {access_to_cooking_text} for cooking in a day.
the client said this for allergies: {client.food_allergies} (DO NOT INCLUDE THIS IN THE DIET AT ANY COST)
the client said this for dislikes foods: {client.disliked_foods} (better not to include in the diet, but if it is necessary, include it)
the client said this for special conditions: {client.special_conditions}
the client said this for prefers kind of food: {preferred_kind_food}
the diet plan you will create should have {plan.plan_rarity} options for each meal.
also, the client said this for meal preference: {plan.meal_preference}
Remeber to generate the diep plan in Fasri language.
"""
    generate_html(question, client_id)

    return {"html": 1, "file_saved": 2}