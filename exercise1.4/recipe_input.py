# Import Pickle module to work with binary files
import pickle

# Function to take user input for recipe components
def take_recipe():
    name = str(input("Enter the name of a recipe: "))
    cooking_time = int(input("Enter the cooking time in minutes: "))
    ingredients = list(input("Enter the ingredients, separated by a comma: ").split(", "))
    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients,
        "difficulty": ""
    }

    # Determines recipe difficulty
    def calc_difficulty():
        if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) < 4:
            recipe["difficulty"] = "Easy"
        elif recipe["cooking_time"] < 10 and len(recipe["ingredients"]) >= 4:
            recipe["difficulty"] = "Medium"
        elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) < 4:
            recipe["difficulty"] = "Intermediate"
        elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) >= 4:
            recipe["difficulty"] = "Hard"

    calc_difficulty()

    return recipe


# Tries to load user-defined filename
file_name = input("Enter a filename to read: ")

try:
    file = open(file_name, "rb")
    data = pickle.load(file)
    print("File loaded.")

# If user-defined filename not found, creates a new one with data dictionary
except FileNotFoundError:
    print("File with that name not found. Creating new file...")
    data = {
        "recipes_list": [],
        "all_ingredients": []
    }

# If other error occurs, performs same operations as previous
except:
    print("Oops, we've stumbled on some unexpected error.")
    data = {
        "recipes_list": [],
        "all_ingredients": []
    }

# Closes file stream
else:
    file.close()

# Extracts values from data dictionary
finally:
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]


# Initial user prompt
n = int(input("How many recipes would you like to enter? "))

# Iterates through number of given recipes
for i in range(n):
    recipe = take_recipe()
    
    # Checks whether an ingredient should be added to all ingredients
    for ingredient in recipe["ingredients"]:
        if not ingredient in all_ingredients:
            all_ingredients.append(ingredient)

    recipes_list.append(recipe)
    print("Recipe added.")


# Gathers the updated data into a new dictionary
data = {
    "recipes_list": recipes_list,
    "all_ingredients": all_ingredients
}

# Opens the user-defined filename and writes to it
updated_file = open(file_name, "wb")
pickle.dump(data, updated_file)
updated_file.close()
print("File updated.")