import pandas as pd

# Load dataset
recipes_data = pd.read_csv('recipes.csv')
# Function to filter recipes based on user preferences
def recommend_recipes(ingredients, diet, cuisine):
    recommended_recipes = []
    for index, row in recipes_data.iterrows():
        # Check if ingredients match
        recipe_ingredients = str(row['ingredients']).lower()
        if all(ingredient.lower() in recipe_ingredients for ingredient in ingredients):
            # Check if diet restriction matches
            if diet.lower() in str(row['diet']).lower() or diet.lower() == 'none':
                # Check if cuisine matches
                if cuisine.lower() in str(row['cuisine']).lower() or cuisine.lower() == 'none':
                    recommended_recipes.append(row['recipe_title'])
    return recommended_recipes

# Take user input
user_ingredients = input("Enter ingredients: ").split(',')
print(user_ingredients)
user_diet = input("Enter diet restriction (e.g., vegan, vegetarian, none): ")
user_cuisine = input("Enter preferred cuisine (e.g., Italian, Mexican, none): ")

# Get recommended recipes
recommended_recipes = recommend_recipes(user_ingredients, user_diet, user_cuisine)

# Display recommendations
if recommended_recipes:
    print("Recommended recipes:")
    for recipe in recommended_recipes:
        print(recipe)
else:
    print("No recipes found matching your preferences.")
