import streamlit as st
import pandas as pd

# Data of Recipes with Ingredients and Nutritional Information
recipes_data = {
    'Recipe': ['Grilled Salmon', 'Chicken Stir-Fry', 'Vegetarian Chili', 'Quinoa Salad'],
    'Ingredients': ['salmon, lemon, garlic, olive oil', 'chicken, vegetables, soy sauce, ginger', 'beans, tomatoes, onions, bell peppers', 'quinoa, cucumber, tomatoes, feta cheese'],
    'Calories': [300, 400, 250, 200],
    'Protein (g)': [25, 30, 15, 10],
    'Carbs (g)': [10, 20, 30, 15],
}

recipes_df = pd.DataFrame(recipes_data)

# Sidebar - User Input
st.sidebar.title('Recipe Suggestion App')
diet_preference = st.sidebar.selectbox('Select Dietary Preference', ['Any', 'Vegetarian', 'Non-Vegetarian'])
available_ingredients = st.sidebar.text_input('Enter Available Ingredients (comma separated)', '')
max_calories = st.sidebar.number_input('Enter Maximum Calories', min_value=0)
min_protein = st.sidebar.number_input('Enter Minimum Protein (g)', min_value=0)
min_carbs = st.sidebar.number_input('Enter Minimum Carbs (g)', min_value=0)

# Filter Recipes based on User Input
filtered_recipes = recipes_df.copy()

if diet_preference != 'Any':
    if diet_preference == 'Vegetarian':
        filtered_recipes = filtered_recipes[filtered_recipes['Ingredients'].str.contains('chicken') == False]
    else:
        filtered_recipes = filtered_recipes[filtered_recipes['Ingredients'].str.contains('chicken')]

if available_ingredients:
    for ingredient in available_ingredients.split(','):
        filtered_recipes = filtered_recipes[filtered_recipes['Ingredients'].str.contains(ingredient.strip())]

filtered_recipes = filtered_recipes[(filtered_recipes['Calories'] <= max_calories) & 
                                    (filtered_recipes['Protein (g)'] >= min_protein) & 
                                    (filtered_recipes['Carbs (g)'] >= min_carbs)]

# Display Suggested Recipes
st.title('Suggested Recipes')
if filtered_recipes.empty:
    st.warning('No recipes found matching the criteria. Please adjust your preferences.')
else:
    st.table(filtered_recipes[['Recipe', 'Ingredients', 'Calories', 'Protein (g)', 'Carbs (g)']])