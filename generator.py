import streamlit as st

# Title of the app
st.title('Word "A" Checker')

# Text input for user to enter the word
user_input = st.text_input("Enter a word:", "")

# Function to check if the word contains 'a'
def check_for_a(word):
    return 'a' in word.lower()  # lower() is used to make it case-insensitive

# Button to perform the check
if st.button('Check for "A"'):
    # If the button is clicked, check if the entered word contains 'a'
    if check_for_a(user_input):
        st.success(f'Yes, the word "{user_input}" contains the letter "a".')
    else:
        st.error(f'No, the word "{user_input}" does not contain the letter "a".')

# Optional: Instructions or information about the app
st.write("This app checks if the entered word contains the letter 'a'.")