from sqlalchemy import Column, Integer, String, Numeric, Text, Date
from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Client(Base):
    __tablename__ = "clients"

    client_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    current_weight_kg = Column(Numeric(5, 2), nullable=False)
    height_cm = Column(Numeric(5, 2), nullable=False)
    gender = Column(Integer, nullable=False)
    age = Column(Integer, nullable=False)
    activity_level = Column(Integer, nullable=True)
    body_fat_percentage = Column(Numeric(5, 2), nullable=True)
    last_program_id = Column(Integer, nullable=True)
    meal_preference = Column(Integer, nullable=False, default=0)
    food_allergies = Column(Text, nullable=True)
    disliked_foods = Column(Text, nullable=True)
    special_conditions = Column(Text, nullable=True)

    # 🔗 One client, many plans
    plans = relationship("Plan", back_populates="client", cascade="all, delete-orphan")


class Plan(Base):
    __tablename__ = "diet_plans"

    plan_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey("clients.client_id"), nullable=False)

    duration = Column(Integer, nullable=True)
    current_weight = Column(Integer, nullable=True)
    goal_weight = Column(Integer, nullable=True)
    type_of_plan = Column(Integer, nullable=True)
    create_date = Column(Date, nullable=True)
    target_calorie_pr = Column(Integer, nullable=True)
    meal_frequency = Column(Integer, nullable=True)
    meal_preference = Column(String(255), nullable=True)
    meal_avoids = Column(String(255), nullable=True)
    special_cases = Column(String(255), nullable=True)
    preferred_kind_food = Column(String(255), nullable=True)
    access_to_cooking = Column(Integer, nullable=True)
    plan_file_path = Column(Text, nullable=True)
    plan_rarity = Column(Integer, nullable=True)

    # 🔙 Connect back to Client
    client = relationship("Client", back_populates="plans")