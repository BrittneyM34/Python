from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func
from sqlalchemy.sql import select

# Database Configuration: Set up connection parameters for the MySQL database.
username = "cf-python"
password = "password"
host = "localhost"
database = "task_database"

# Connect SQLAlchemy with the database
engine = create_engine("mysql://cf-python:password@localhost/task_database")

# Create the session
Session = sessionmaker(bind=engine)
session = Session()

# Create Declarative Base
Base = declarative_base

# Define recipe model
class Recipe(Base):
    __tablename__ = "final_recipes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    # Used for debugging purposes
    def __repr__(self):
        return f"<Recipe ID: {self.id} - {self.name} - {self.difficulty}>"
    
    # Formats recipe details for printing
    def __str__(self):
        ingredients_list = self.ingredients.split(", ")
        formatted_ingredients = "\n ".join(f" - {ingredient.title()}" for ingredient in ingredients_list)

        return (f"Recipe ID: {self.id}\n"
                f" Name: {self.name.title()}\n"
                f" Ingredients:\n {formatted_ingredients}"
                f" Cooking Time: {self.cooking_time} minutes\n"
                f" Difficulty: {self.difficulty}\n")
    
    #Method to calculate difficulty
    def calculate_difficulty(self):
    num_ingredients = len(ingredients)
    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    elif cooking_time >= 10 and num_ingredients <= 4:
        return "Hard"