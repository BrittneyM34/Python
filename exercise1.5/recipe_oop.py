class Recipe(object):

    all_ingredients = []

    def __init__(self, name, ingredients, cooking_time):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.difficulty = ""

    # Getter methods
    def get_name(self):
        return self.name
    
    def get_cooking_time(self):
        return self.cooking_time
    
    # Setter methods
    def set_name(self, name):
        self.name = name

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    # a method called add_ingredients that takes in variable number of arguments and adds them to the recipe's ingredients
    def add_ingredients(self, *ingredients):
        self.ingredients.append(ingredients)
        self.update_all_ingredients()

    # getter method for ingredients 
    def get_ingredients(self):
        return self.ingredients
        
    def calculate_difficulty(self, cooking_time, ingredients):
        if (cooking_time < 10) and (len(ingredients) < 4):
            difficulty_level = "Easy"
        elif (cooking_time < 10) and (len(ingredients) >= 4):
            difficulty_level = "Medium"
        elif (cooking_time >= 10) and (len(ingredients) < 4):
            difficulty_level = "Intermediate"
        elif (cooking_time >= 10) and (len(ingredients) >= 4):
            difficulty_level = "Hard"
        else:
            print("Something bad happened, please try again")
        return difficulty_level
    
    def get_difficulty(self): 
        if not self.difficulty:
            self.calculate_difficulty()
        return self.difficulty
    
    # A search method
    def search_ingredients(self, ingredient, ingredients):
        if ingredient in self.ingredients:
            return True
        else: 
            return False
        
    # A method called update_all_ingredients() that updates the all_ingredients list
    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in self.ingredients:
                self.all_ingredients.append(ingredient)
        
    # A string representation that prints the entire recipe over a well formatted string
    def __str__(self):
        output = "Name: " + self.name + \
            "\nIngredients: " + str(self.ingredients) + \
            "\nCooking Time: " + str(self.cooking_time) + \
            "\nDifficulty: " + str(self.difficulty) + \
            "\n-----------------------------"
        for ingredient in self.ingredients:
            output += " - " + ingredient + "\n"
            return output
        
    def recipe_search(self, recipes_list, ingredient):
        data = recipes_list
        search_term = ingredient
        for recipe in data:
            if self.search_ingredients(search_term, recipe.ingredients):
                print(recipe)

# Create recipes
tea = Recipe("Tea", ["Tea Leaves", "Sugar", "Water"], 5)
coffee = Recipe("Coffee", ["Coffee Powder", "Sugar", "Water"], 5)
cake = Recipe("Cake", ["Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"], 50)
banana_smoothie = Recipe("Banana Smoothie", ["Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"], 5)

# Add recipes to list
recipes_list = [tea, coffee, cake, banana_smoothie]

# Display representation of each recipe
for recipe in recipes_list:
    print(recipe)

# Search for recipes that contain certain ingredients
print("--------------------------")
print("Recipes List")
print("--------------------------")
for recipe in recipes_list:
    print(recipe)

print("--------------------------")
print("Results for recipe_search with Water: ")
print("--------------------------")
tea.recipe_search(recipes_list, "Water")

print("--------------------------")
print("Results for recipe_search with Sugar: ")
print("--------------------------")
tea.recipe_search(recipes_list, "Sugar")

print("--------------------------")
print("Results for recipe_search with Bananas: ")
print("--------------------------")
tea.recipe_search(recipes_list, "Bananas")