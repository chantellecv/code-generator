import streamlit as st

# App title
st.title('Letter "C" Checker')

# Text input for the user to enter a word
user_word = st.text_input("Enter a word:", "")

# Function to check if 'c' is in the word
def check_for_c(word):
    return 'c' in word.lower()  # Case-insensitive check

# Display result when a word is entered
if user_word:  # Runs if user_word is not empty
    if check_for_c(user_word):
        st.success(f'Yes, the word "{user_word}" contains the letter "c".')
    else:
        st.error(f'No, the word "{user_word}" does not contain the letter "c".')