# app.py

import streamlit as st

# App title
st.title('Does it contain "e"?')

# Text input from user
user_input = st.text_input("Enter a word:")

# Function to check if the word contains 'e'
def contains_e(word):
    return 'e' in word.lower()

# Display the result
if user_input:  # Check if there is user input
    result = contains_e(user_input)
    if result:
        st.success(f'Yes, "{user_input}" contains the letter "e".')
    else:
        st.error(f'No, "{user_input}" does not contain the letter "e".')