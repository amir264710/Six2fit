from sqlalchemy import Column, Integer, String, Numeric, Text
from database import Base

class Client(Base):
    __tablename__ = "clients"

    client_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    current_weight_kg = Column(Numeric(5,2), nullable=False)
    height_cm = Column(Numeric(5,2), nullable=False)
    gender = Column(Integer, nullable=False)
    age = Column(Integer, nullable=False)
    activity_level = Column(Integer, nullable=True)
    body_fat_percentage = Column(Numeric(5,2), nullable=True)
    last_program_id = Column(Integer, nullable=True)
    meal_preference = Column(Integer, nullable=False, default=0)
    food_allergies = Column(Text, nullable=True)
    disliked_foods = Column(Text, nullable=True)
    special_conditions = Column(Text, nullable=True)
