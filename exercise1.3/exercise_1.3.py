# Empty lists
recipes_list = []
ingredients_list = []

# Defining function
def take_recipe():
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time in minutes: "))
    ingredients = list(input("Enter the ingredients, separated by a comma: ").split(", "))

    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients
    }
    return recipe

# User prompt
n = int(input("How many recipes would you like to enter? "))

# Iterates through number of given recipes
for i in range(n):
    recipe = take_recipe()
    # Checks if an ingredient should be added
    for ingredient in recipe["ingredients"]:
        if not ingredient in ingredients_list:
            ingredients_list.append(ingredient)

    recipes_list.append(recipe)

# Iterates through recipe list to determine difficulty
for recipe in recipes_list:
    if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) < 4:
        recipe["difficulty"] = "Easy"
    elif recipe["cooking_time"] < 10 and len(recipe["ingredients"]) >= 4:
        recipe["difficulty"] = "Medium"
    elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) < 4:
        recipe["difficulty"] = "Intermediate"
    elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) >= 4:
        recipe["difficulty"] = "Hard"

# Iterates through recipes_list to display their information
for recipe in recipes_list:
    print("Recipe: ", recipe["name"])
    print("Cooking time (minutes): ", recipe["cooking_time"])
    print("Ingredients: ")
    for ingredient in recipe["ingredients"]:
        print(ingredient)
    print("Difficulty level ", recipe["difficulty"])

# Display all ingredients in alphabetical order
def all_ingredients():
    print("All ingredients available")
    print("===========")
    ingredients_list.sort()
    for ingredient in ingredients_list:
        print(ingredient)

all_ingredients()