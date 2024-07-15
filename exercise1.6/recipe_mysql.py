import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "cf-python",
    passwd = "password"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

cursor.execute("USE task_database")

cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
               id INT AUTO_INCREMENT PRIMARY KEY,
               name VARCHAR(50),
               ingredients VARCHAR(255),
               cooking_time INT,
               difficulty VARCHAR(20)
)''')

def main_menu(conn, cursor):
    choice = ""
    while(choice != 'quit'):
        print("What would you like to do? Pick a choice!")
        print("1. Create a recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe\n")
        print("Type 'quit' to exit the program")
        choice = input("Your choice: ")
        print()

        if choice =='1':
            create_recipe(conn, cursor)
        elif choice =='2':
            search_recipe(conn, cursor)
        elif choice =='3':
            update_recipe(conn, cursor)
        elif choice =='4':
            delete_recipe(conn, cursor)
        elif choice == "quit":
            print("Thanks for using the recipe app! Come again soon")
        else: 
            print("Invalid choice, please choose option 1, 2, 3, 4, or quit")

            conn.close

def create_recipe(conn, cursor):
    print()
    print("** Create New Recipes **")
    
    while True:
        try:
            number_of_recipes = int(input("How many recipes would you like to enter? "))
            if number_of_recipes < 1:
                print("Please enter a positive number. \n")
            else: 
                break
        except ValueError:
            print("Invalid input. Please enter a number")

    for i in range(number_of_recipes):
        print(f"Enter recipe #{i + 1}")
        print("-------------------------")

        name = input(" Enter the recipe name: ")
        cooking_time = int(input(" Enter the cooking time in minutes: "))
        ingredients_input = input(" Enter the recipe's ingredients, separateed by a comma: ")
        ingredients = ingredients_input.split(", ")

        difficulty = calculate_difficulty(cooking_time, ingredients)

        ingredients_str = ", ".join(ingredients)

        try: 
            insert_query = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (name, ingredients_str, cooking_time, difficulty))
            conn.commit()

            print(" ------------------------------- ")
            print(" ** Recipe added succesfully! ** ")
            print(" ------------------------------- ")

        except mysql.connector.Error as err:
            print("Error occurred: ", err)

def calculate_difficulty(cooking_time, ingredients):
    num_ingredients = len(ingredients)
    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    elif cooking_time >= 10 and num_ingredients <= 4:
        return "Hard"
    
def recipe_display(recipe):
    print(f"\nRecipe: {recipe[1].title()}")
    print(f" Time: {recipe[3]} minutes")
    print(f" Ingredients: ")
    for ingredient in recipe[2].split(", "):
        print(f" - {ingredient.title()}")
    print(f" Difficulty: {recipe[4]}")

def search_recipe(conn, cursor):
    # Fetch ingredients from table
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()

    if not results: 
        print(" ----------------------------------------------------------------------- ")
        print(" **There are no recipes in this database. Please create a new recipe! ** ")
        print(" ----------------------------------------------------------------------- ")
        print(" Returning to main menu... ")
        return
    
    all_ingredients = set()

    print()
    print(" --------------------------------------- ")
    print(" ** Search for a recipe by ingredient ** ")
    print(" --------------------------------------- ")
    print("Please enter a number to see all recipes that use that ingredient\n")

    # Loop through results
    for result in results:
        ingredients_list = result[0].split(", ")
        for ingredient in ingredients_list:
            all_ingredients.add(ingredient.strip())

    for i, ingredient in enumerate(sorted(all_ingredients)):
        print(f"{i+1}.) {ingredient.title()}")

    #Remove duplicates from the list
    all_ingredients = list(dict.fromkeys(all_ingredients))

    print()
    while True:
        try:
            choice = int(input("Enter a number for the ingredient"))
            if 1 <= choice <= len(all_ingredients):
                break
            else:
                print()
                print("Please print a number within the range")
        except ValueError:
            print()
            print("Invalid input. Please enter a number")

        selected_ingredient = sorted(all_ingredients[choice - 1])
         
        search_ingredient = "SELECT * FROM Recipes WHERE ingredients LIKE %s"
        cursor.execute(search_ingredient, ("%" + selected_ingredient + "%"))
        search_results = cursor.fetchall()

        if search_results:
            recipe_count = len(search_results)
            recipe_word = "recipe" if recipe_count == 1 else "recipes"
            print(f"\n{recipe_count} {recipe_word} found containing'{selected_ingredient.title()}'\n")
            for recipe in search_results:
                recipe_display(recipe)

            print()
            print("----------------------------- ")
            print(" **Recipe search successful** ")
            print("----------------------------- ")
            print("..returning to the main menu")
        else:
            print(f"No recipes found containing that ingredient")

def update_recipe(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()

    if not results: 
        print(" ----------------------------------------------------------------------- ")
        print(" **There are no recipes in this database to update. Please create a new recipe! ** ")
        print(" ----------------------------------------------------------------------- ")
        print(" Returning to main menu... ")
        return

    print()
    print(" --------------------------------------- ")
    print(" ** Update a recipe by ID number ** ")
    print(" --------------------------------------- ")
    print("Please enter an ID number to update that recipe\n")

    print(" **Available recipes** ")

    for result in results: 
        ingredients_list = result[2].split(", ")
        capitalized_ingredients = [ingredient.title() for ingredient in ingredients_list]
        capitalized_ingredients_str = ", ".join(capitalized_ingredients)

        print(f"ID: {result[0]} | Name: {result[1]}")
        print(f"Ingredients: {capitalized_ingredients_str} | Cooking Time: {result[3]} | Difficulty: {result[4]}\n")

    while True:
        try: 
            print()
            recipe_id = int(input("Enter the ID of the recipe to update: "))
            print()

            cursor.execute("SELECT COUNT(*) FROM Recipes WHERE id = %s", (recipe_id,))
            if cursor.fetchone()[0] == 0:
                print("No recipe found with the entered ID, please try again\n")
            else:
                break
        except ValueError:
            print()
            print("Invalid input. Please enter a number\n")

    selected_recipe = next((recipe for recipe in results if recipe[0] == recipe_id), None)
    if selected_recipe:
         print(f"Which field would you like to update for '{selected_recipe[1]}'?")
    else:
        print("Recipe not found")
        return
    print(" - Name")
    print(" - Cooking Time")
    print(" - Ingredients\n")

    if update_field == "cooking time":
        update_field = "cooking_time"

    if update_field not in["name", "cooking_time", "ingredients"]:
        print("Invalid field. Please enter 'name', 'cooking_time', or 'ingredients'")
        return
    
    if update_field == "cooking_time":
        while True:
            try:
                new_value = int(input("Enter the new cooking time in minutes: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number for cooking time")
    else:
        new_value = input(f"Enter the new value for {update_field}: ")

        update_query = f"UPDATE Recipes SET {update_field}: "
        cursor.execute(update_query(new_value, recipe_id))

        if update_field in ["cooking_time", "ingredients"]:
            cursor.execute("SELECT cooking_time, ingredients")

        if update_field in ["cooking_time", "ingredients"]:
            cursor.execute("SELECT cooking_time, ingredients FROM Recipes WHERE id=%s", (recipe_id,))
            updated_recipe = cursor.fetchone()
            new_difficulty = calculate_difficulty(int(updated_recipe[0]), updated_recipe[1].split(", "))

            cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (new_difficulty, recipe_id))

            conn.commit()

            print()
            print("-----------------------------------------")
            print(" **Recipe updated successfully** ")
            print("-----------------------------------------")
            print("Returning to main menu...")

def delete_recipe(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()

    if not results:
        print(" ----------------------------------------------------------------------- ")
        print(" **There are no recipes in this database to update. Please create a new recipe! ** ")
        print(" ----------------------------------------------------------------------- ")
        print(" Returning to main menu... ")
        return

    print()
    print(" --------------------------------------- ")
    print(" ** Delete a recipe by ID number ** ")
    print(" --------------------------------------- ")
    print("Please enter an ID number to delete that recipe\n")
    print("This can NOT be undone")

    print(" **Available recipes** ")

    for result in results:
        ingredients_list = result[2].split(", ")
        capitalized_ingredients = [ingredient.title() for ingredient in ingredients_list]
        capitalized_ingredients_str = ", ".join(capitalized_ingredients)

        print(f"ID: {result[0]} | Name: {results[1]}")
        print(f"Ingredients: {capitalized_ingredients_str} | Cooking Time: {result[3]} | Difficulty: {result[4]}\n")

        while True:
            try: 
                recipe_id = int(input("Enter the ID of the recipe to delete: "))
                print()

                cursor.execute("SELECT COUNT(*) FROM Recipes Where id = %s", (recipe_id,))
                if cursor.fetchone()[0] == 0:
                    print("No recipe found with the entered ID. Please try again.\n")
                else:
                    cursor.execute("SELECT name FROM Recipes WHERE id= %s", (recipe_id,))
                    recipe_name = cursor.fetchone()[0]
                    confirm = input(f"Are you sure you want to delete '{recipe_name}'? (Yes/No): ".lower())

                    if confirm == "yes":
                        break
                    elif confirm == "no":
                        print()
                        print("Deletion cancelled. Returning to main menu...")
                        return
                    else:
                        print()
                        print("Please enter answer with 'yes' or 'no'.")

            except ValueError:
                print("Invalid input. Please enter a numeric value")

        cursor.execute("DELETE FROM Recipes WEHRE id = %s", (recipe_id,))

        conn.commit()

        print()
        print("----------------------------")
        print(" **Recipe Deleted** ")
        print("----------------------------")   
        print("Returning to main menu....")

        main_menu(conn, cursor)     

