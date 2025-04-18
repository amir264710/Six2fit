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
        "No workout" if client.activity_level == 1
        else "Slightly active" if client.activity_level == 2
        else "Active" if client.activity_level == 3
        else "Unknown"
    )
    meal_preference = (
        "Vegetarian" if client.meal_preference == 1
        else "Vegan" if client.meal_preference == 2
        else "Non-Vegetarian" if client.meal_preference == 3
        else "Unknown"
    )

    access_to_cooking_text= (
        "very much" if plan.access_to_cooking == 1
        else "slightly" if plan.access_to_cooking == 2
        else "maybe not so much"
    )

    # Build the client data as an f-string
    client_data = f"""
Client Data:
- current_weight_kg: {client.current_weight_kg}
- height_cm: {client.height_cm}
- gender: {gender_text}
- age: {client.age}
- activity_level: {activity_text}
- body_fat_percentage: {client.body_fat_percentage}
- meal_preference: local
- food_allergies: {client.food_allergies} (DO NOT INCLUDE THIS IN THE DIET AT ANY COST)
- disliked_foods: {client.disliked_foods} (better not to includec in the diet)
- special_conditions: {client.special_conditions}
"""

    # Build the plan data as an f-string using the plan payload
    plan_data = f"""
Plan Data:
- current_weight: {plan.current_weight}
- goal_weight: {plan.goal_weight}
- target_calorie_pr: {plan.target_calorie_pr} (in single day)
- meal_frequency: 3 (how much meals per day, include main course and snacks)
- meal_avoids: {plan.meal_avoids}
- meal_options: 3 (how much options per meal)
- special_cases: {plan.special_cases}
- preferred_kind_food: {plan.preferred_kind_food}
- access_to_cooking: {access_to_cooking_text}
- plan_file_path: {plan.plan_file_path}
- plan_rarity: {plan.plan_rarity}
"""

    # Compose the complete question with instructions as an f-string
    question = f"""
Based on the following client data and plan data, generate a personalized and detailed diet plan in a complete HTML document.
Your output must include only HTML code without any additional commentary or text. (DOUABLE CHECK FOR THE DIET TO NOT 
HAVE ANY OF THE food_allergies IN IT). Also, make each meal option has the ingredients and approximate calories for each meal.
and the client is from Iran, so the diet should be based on Iranian food and ingredients. and also make the language of the diet plan in Persian.


{client_data}

{plan_data}

Instructions:
1. Create a full HTML document with proper tags, including <!DOCTYPE html>, <html>, <head> (with a <title>) and <body>.
2. Structure the HTML to clearly showcase the best diet plan tailored for this client (make it looks good, clean and have some emoji).
3. Output only the HTML code.
"""
    generate_html(question, client_id)

    return {"html": 1, "file_saved": 2}