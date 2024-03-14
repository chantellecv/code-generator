import streamlit as st

# Function to check if the word is a palindrome
def is_palindrome(word):
    # Removing spaces and converting to lowercase to ensure accuracy
    clean_word = word.replace(" ", "").lower()
    return clean_word == clean_word[::-1]

# Streamlit app layout
st.title('Palindrome Checker')
# Input field for the user to enter a word
word = st.text_input('Enter a word to check if it is a palindrome')

# When the user has entered a word
if word:
    # Check if the word is a palindrome
    result = is_palindrome(word)
    if result:
        st.success(f'"{word}" is a palindrome!')
    else:
        st.error(f'"{word}" is not a palindrome.')