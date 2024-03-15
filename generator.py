# First, import the necessary library
import streamlit as st

# Title for your app
st.title('Word "i" Checker App')

# Taking a word input from the user
user_input = st.text_input('Enter a word:')

# Function to check if the word contains 'i' or 'I'
def contains_i(word):
    return 'i' in word.lower()  # This makes the check case-insensitive

# Display result when the user has entered a word
if user_input:  # Checks if the string is not empty
    if contains_i(user_input):
        st.write(f'The word "{user_input}" contains the letter "i".')
    else:
        st.write(f'The word "{user_input}" does not contain the letter "i".')