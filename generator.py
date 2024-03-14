# Importing Streamlit
import streamlit as st

# Function to check if a word is a palindrome
def is_palindrome(word):
    # Removing spaces and converting to lowercase for accurate comparison
    cleaned_word = word.replace(" ", "").lower()
    return cleaned_word == cleaned_word[::-1]

# Streamlit application
def app():
    # Title of the app
    st.title("Palindrome Checker")

    # User input
    word = st.text_input("Enter a word to check if it's a palindrome:")

    if word:  # If user has entered a word
        result = is_palindrome(word)  # Check if it is a palindrome
        if result:
            st.success(f"✅ '{word}' is a palindrome!")
        else:
            st.error(f"❌ '{word}' is not a palindrome.")

# Run the app
if __name__ == "__main__":
    app()