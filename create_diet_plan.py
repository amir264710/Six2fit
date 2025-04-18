import openai

# Replace with your actual OpenAI API key
openai.api_key = "your-api-key-here"

# Your input question
question = """
Based on the following client and plan data, generate a personalized and detailed diet plan in a complete HTML document. Your output must include only HTML code without any additional commentary or text.

Client Data:
- current_weight_kg: Current weight in kilograms.
- height_cm: Height in centimeters.
- gender: Gender
- age: Age in years.
- activity_level: Activity level (may be null).
- body_fat_percentage: Body fat percentage (may be null).
- last_program_id: Identifier of the last program (may be null).
- meal_preference: Meal preference (default is 0).
- food_allergies: Any food allergies (may be null).
- disliked_foods: Foods the client dislikes (may be null).
- special_conditions: Any special medical or dietary conditions (may be null).

Plan Data:
- current_weight: Current weight as recorded in the plan.
- goal_weight: Target weight goal.
- type_of_plan: Type of diet plan.
- create_date: Date when the plan was created.
- target_calorie_pr: Target daily calorie intake.
- meal_frequency: Number of meals per day.
- meal_preference: Detailed meal preferences in the plan.
- meal_avoids: Foods or ingredients to avoid.
- special_cases: Special cases or dietary needs.
- preferred_kind_food: Preferred type of food.
- access_to_cooking: Indicator of access to cooking facilities.
- plan_file_path: File path reference for the plan (if available).
- plan_rarity: A measure of how unique the plan is.

Instructions:
1. Create a full HTML document with proper tags, including <!DOCTYPE html>, <html>, <head> (with a <title>), and <body>.
2. Structure the HTML to clearly showcase the best diet plan tailored for this client. Use headers, paragraphs, and lists where appropriate to organize sections like "Overview," "Daily Meal Plan," "Nutritional Breakdown," and any other relevant sections.
3. Ensure that the response contains only the HTML code and nothing else.

Output only the HTML code.
"""

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
    messages=[
        {"role": "system", "content": "You are a highly experienced nutritionist and web developer with expertise in generating personalized, data-driven diet plans. Use your skills to produce a comprehensive and visually-structured HTML document that outlines the best diet plan for the client based on the provided data. Your output must strictly be valid HTML code with no extra commentary, explanations, or text beyond the HTML."},
        {"role": "user", "content": question}
    ]
)
# Extract the response text
answer = response.choices[0].message.content

# Save response to a file
with open("chatgpt_response.txt", "w", encoding="utf-8") as file:
    file.write(answer)

print("✅ Response saved to chatgpt_response.txt")
