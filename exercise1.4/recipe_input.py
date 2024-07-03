import pickle

def take_recipe():
    name = str(input("Enter the name of the recipe: "))
    cooking_time = int(input("Enter the cooking time in minutes: "))
    ingredients = list(input("Enter the ingredients, separated by a comma: ").split(", "))

    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients
    }