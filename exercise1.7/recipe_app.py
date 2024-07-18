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
Base = declarative_base()

# Define recipe model
class Recipe(Base):
    __tablename__ = "final_recipes"
    id = Column(Integer, primary_key=True)
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
        ingredient_list = self.return_ingredients_as_list()
        num_ingredients = len(ingredient_list)
        if self.cooking_time < 10 and num_ingredients < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and num_ingredients >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and num_ingredients < 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and num_ingredients <= 4:
            self.difficulty = "Hard"

    # Convert Ingredients to List: Splits the ingredients string into a list for easier manipulation.
    def return_ingredients_as_list(self):
        if not self.ingredients:
            return []
        return self.ingredients.split(", ")
    
# Create tables
Base.metadata.create_all(engine)

def create_recipe():
    print()
    print("-----------------------------")
    print(" ** Create New Recipes ** ")
    print("-----------------------------")
    print("Please follow the steps below to add new recipes!\n")

    # Loop to get the number of recipes the user wants to enter.
    # Validates that the input is a positive integer.
    while True:
        try: 
            number_of_recipes = int(input("How many recipes would you like to enter? "))
            if number_of_recipes < 1:
                print("Please enter a positive number")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number")

    # Loop over the number of recipes to be created
    for i in range(number_of_recipes):
        print(f"\nEnter recipe #{i + 1}")
        print("---------------------------")

        # Input validation for recipe name, ensure it is within the character limit
        while True:
            name = input("Enter the recipe name: ").strip()
            if 0 < len(name) <= 50:
                break
            else: 
                print("Please enter a valid recipe name within 1-50 characters/")

        # Input validation for cooking time
        while True:
            try:
                cooking_time = int(input("Enter the cooking time in minutes: "))
                if cooking_time > 0:
                    break
                else:
                    print("Please enter a positive number for cooking time.\n")
            except ValueError:
                print("Invalid input. Please enter a positive number for cooking time.\n")

        # Input validation for ingredients, ensuring the input is not empty
        while True:
                ingredients_input = input("Enter the recipe's ingredients, separated by a comma: ").strip()
                if ingredients_input:
                    break
                else: 
                    print("Please enter at least one ingredient")

        #Create a new recipe instance and add it to the session
        new_recipe = Recipe(name=name, ingredients=ingredients_input, cooking_time=cooking_time)
        new_recipe.calculate_difficulty()

        # Add the new recipe to the session and commit it to the database
        session.add(new_recipe)
        try: 
            session.commit()
            print(" **Recipe successfully added! **")
        except Exception as err:
            session.rollback()
            print("Error occurred: ", err)

def view_all_recipes():
    # Retrieve all recipes from the database
    recipes = session.query(Recipe).all()

    # Check if there are recipes in the database
    if not recipes:
        print("----------------------------------------------------")
        print(" ** There are no recipes to view in the database ** ")
        print("----------------------------------------------------")
        return None
    
    print("------------------------")
    print(" ** View all recipes ** ")
    print("------------------------")

    # Display the recipes found
    recipe_count = len(recipes)
    recipe_word = "recipe" if recipe_count == 1 else "recipes"
    print(f"Displaying {recipe_count} {recipe_word}\n")

    # Loop through each recipe and display its details using a formatted string
    for i, recipe in enumerate(recipes, start=1):
        print(f"Recipe #{i}\n")
        print(format_recipe_for_search(recipe))
        print()

    # End of listing display after listing all recipes
    print()
    print(" ** List Display successful ** ")
    print("--------------------------------")



def view_recipes():
    # retrieve recipes form the database
    recipes = session.query(Recipe).all()

    # Check if there are any recipes in the database
    if not recipes: 
        print("--------------------------------------------")
        print("There are no recipes in the database to view")
        print("--------------------------------------------")
        print()
        return None
    
    print("----------------------")
    print(" **View all recipes** ")
    print("----------------------")

    # display the number of recipes found
    recipe_count = len(recipes)
    recipe_word = "recipe" if recipe_count == 1 else "recipes"
    print(f"Displaying {recipe_count} {recipe_word}\n")

    # Loop through each recipe
    for i, recipe in enumerate(recipes, start=1):
        print(f"Recipe #{i}\n")
        print(format_recipe_for_search(recipe))

    print("-----------------------------")
    print(" **List Display Successful** ")
    print("-----------------------------")

def search_recipe():
    # Retrieve all ingredients from all recipes
    results = session.query(Recipe.ingredients).all()

    if not results:
        print("--------------------------------------------")
        print("There are no recipes in the database to search")
        print("--------------------------------------------")
        print()
        return
    
    # Initialize a set to store all ingredients
    all_ingredients = set()
    for result in results:
        ingredients_list = result[0].split(", ")
        for ingredient in ingredients_list:
            all_ingredients.add(ingredient.strip())

    print("---------------------------------------")
    print(" **Search for a recipe by ingredient** ")
    print("---------------------------------------")
    print("Please enter a number to see all recipes that use that ingredient\n")

    # Sort and display each unique ingredient with its corresonding index
    sorted_ingredients = sorted(all_ingredients)
    for i, ingredient in enumerate(sorted_ingredients):
        print(f"{i+1}.){ingredient.title()}")

    # Prompt user to enter one or more ingredient numbers
    print()
    while True:
        try: 
            choices = input("Enter ingredient numbers (separate multiple numbers with spaces): ").split()
            selected_indices = [int(choice) for choice in choices]
            if all(1<= choice <= len(all_ingredients) for choice in selected_indices):
                break
            else:
                print("Please enter numbers within the list range.\n")
        except ValueError:
            print("Invalid input. Please enter valid numbers")

    # Convert user input into a list of selected ingredients
    search_ingredients = [sorted_ingredients[index - 1] for index in selected_indices]

    # Build a search query using the selected ingredeints
    search_conditions = [Recipe.ingredients.ilike(f"%{ingredient}%") for ingredient in search_ingredients]
    search_results = session.query(Recipe).filter(*search_conditions).all()

    # Format the string of selected ingredients
    if len(search_ingredients) > 1:
        selected_ingredients_str = ", ".join(ingredient.title() for ingredient in search_ingredients)
        selected_ingredients_str += ", or " + search_ingredients[-1].title()
    else:
        selected_ingredients_str = search_ingredients[0].title()

    # Check if there are any recipes found with the selected ingredients
    if search_results:
        recipe_count = len(search_results)
        recipe_word = "recipe" if recipe_count == 1 else "recipes"
        print(f"\n{recipe_count} {recipe_word} found containing '{selected_ingredients_str}'\n")

        # Display each recipe found with its details
        for i, recipe in enumerate(search_results, start=1):
            print(f"Recipe #{i}\n----------")
            print(format_recipe_for_search(recipe))
            print()

        print()
        print("--------------------------")
        print(" Recipe Search Successful ")
        print("--------------------------")
    else:
        print(f"No recipes found containing '{selected_ingredients_str}'\n")

def update_recipe(): 
    # Retrieve all recipes from the database
    recipes = session.query(Recipe).all()

    if not recipes: 
        print("--------------------------------------------")
        print("There are no recipes in the database to update")
        print("--------------------------------------------")
        print()
        return 
    
    print()
    print("------------------------------------")
    print(" ** Update a Recipe By ID Number ** ")
    print("------------------------------------")
    print("Please enter an ID number to update that recipe\n")

    # Display the recipes available
    print("Available Recipes: \n")
    for recipe in recipes:
        print(format_recipe_for_update(recipe))
    print()

    # Loop to get the ID of the recipe
    while True:
        try:
            recipe_id = int(input("Enter the ID of the recipe to update: "))
            recipe_to_update = session.get(Recipe, recipe_id)
            if recipe_to_update:
                break
            else: 
                print("No recipe found with the entered ID. Please try again\n")
        except ValueError:
            print("Invalid input. Please enter a numberic value\n")

    # Prompt the user to choose which field of the recipe to update
    print(f"\nWhich field would you like to update for '{recipe_to_update.name}'?")
    print(" - Name")
    print(" - Cooking Time")
    print(" - Ingredients\n")

    # Flag to track whether the field has been successfully updated
    field_updated = False
    while not field_updated:
        update_field = input("Enter your choice: ").lower()

        # Update logic for each field
        if update_field == "name":
            while True: 
                new_value = input("\nEnter the new name (1-50 characters): ").strip()
                if 0 < len(new_value) <= 50:
                    recipe_to_update.name = new_value
                    field_updated = True
                    break
                else: 
                    print("Invalid name. Please enter 1-50 characters\n")
            break

        elif update_field == "cooking time":
            while True:
                try: 
                    new_value = int(input("\nEnter the new cooking time in minutes: "))
                    if new_value > 0:
                        recipe_to_update.cooking_time = new_value
                        # Recalculate the difficulty
                        recipe_to_update.calculate_difficulty()
                        field_updated = True
                        break
                    else: 
                        print("Please enter a positive number for cooking time")
                except ValueError:
                    print("Invalid input. Please enter a numberic value for cooking time")
            break

        elif update_field == "ingredients":
            while True:
                new_value = input("\nEnter the ingredients, separated by a comma: ")
                if new_value:
                    recipe_to_update.ingredients = new_value
                    recipe_to_update.calculate_difficulty()
                    field_updated = True
                    break
                else:
                    print("Please enter at least one ingredients")
            break
        else: 
            print("Invalid choice. Please choose 'name', 'cooking time', or 'ingredients'.")

    # Attempt to commit the updated recipe
    try:
        session.commit()
        print("-----------------------------------")
        print(" ** Recipe Successfully Updated ** ")
        print("-----------------------------------")
    except Exception as err:
        session.rollback()
        print(f"An error occured: {err}")

def delete_recipe():
    # Retrieve all recipes from the database.
    recipes = session.query(Recipe).all()

    if not recipes: 
        print("----------------------------------------------")
        print("There are no recipes in the database to delete")
        print("----------------------------------------------")
        print()
        return 
    
    print()
    print("------------------------------------")
    print(" ** Delete a Recipe By ID Number ** ")
    print("------------------------------------")
    print("Please enter an ID number to delete that recipe\n")
    print(" ** This CANNOT be undone ** ")

    # Display the available recipes for deletion
    print(" Available recipes ")
    for recipe in recipes:
        print(format_recipe_for_update(recipe))

    # Loop to get the ID of the recipe to be deleted
    while True:
        try: 
            recipe_id = int(input("\nEnter the ID of the recipe to be deleted: "))
            recipe_to_delete = session.get(Recipe, recipe_id)

            # Confirm deletion from the user
            if recipe_to_delete:
                confirm = input(f"\nAre you sure you want to delete '{recipe_to_delete.name}'? (Yes/No): ").lower()
                if confirm == "yes":
                    break
                elif confirm == "no":
                    print("Deletion cancelled.\n")
                    return
                else:
                    print("Please answer with 'Yes' or 'No'.")
            else:
                print("No recipe found with the entered ID, please try again")
        except ValueError:
            print("Invalid input. Please enter a numeric value")

    # Attempt to delete from the database
    try:
        session.delete(recipe_to_delete)
        session.commit()
        print()
        print(" ** Recipe Successfully Deleted **")
        print()
    except Exception as err:
        session.rollback()
        print(f"An error occured: {err}")

def main_menu():
    choice = ""

    while choice != "quit":
        print()
        print("===============================================")
        print("           -----Recipe App--------             ")
        print("===============================================")
        print("What would you like to do? Pick a choice below!")
        print("===============================================")
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search for a recipe by ingredient")
        print("4. Update an existing recipe")
        print("5. Delete a recipe")
        print("Type 'quit' to exit the program")

        # Get the user's choice and convert it to lower case
        choice = input("Your choice: ").strip().lower()

        # Execute the appropriate function based on the user's choice
        if choice == "1":
            create_recipe()
        elif choice == "2":
            view_all_recipes()
        elif choice == "3":
            search_recipe()
        elif choice == "4":
            update_recipe()
        elif choice == "5":
            delete_recipe()
        elif choice == "quit":
            print("=================================")
            print(" Thanks for using the recipe app!")
            print("       See you next time!        ")
            print("=================================")
            break
        else:
            print("--Invalid choice! Please enter 1, 2, 3, 4, 5, or 'quit'")

    session.close()
    engine.dispose()

def format_recipe_for_search(recipe):
    # Format the ingredients for display
    formatted_ingredients = "\n ".join(f"- {ingredient.title()}" for ingredient in recipe.ingredients.split())

    # Return a formatted string representing the recipes details
    return(f" Recipe Name: {recipe.name.title()}\n"
           f" Cooking Time: {recipe.cooking_time}\n"
           f" Ingredients: {formatted_ingredients}\n"
           f" Difficulty: {recipe.difficulty}\n")

def format_recipe_for_update(recipe):
    # Capitalize the first letter of each ingredient
    capitalized_ingredients = [ingredient.title() for ingredient in recipe.ingredients.split(", ")]
    capitalized_ingredients_str = ", ".join(capitalized_ingredients)

    # Return a formatted string representing the details
    return (f"ID: {recipe.id} | Name: {recipe.name}\n"
            f"Ingredients: {capitalized_ingredients_str} | Cooking Time: {recipe.cooking_time} | Difficulty: {recipe.difficulty}\n")

if __name__ == "__main__":
    main_menu()