import streamlit as st
import re

# Function to check if a word is a palindrome
def is_palindrome(word):
    word = re.sub(r'\W+', '', word).lower()
    return word == word[::-1]

# Streamlit app
if __name__ == "__main__":
    st.title("Palindrome Checkerrrrr")

    word_input = st.text_input("Enter a word to check for palindromity:")

    if st.button("Check"):
        if not word_input:
            st.write("Please enter a word.")
        else:
            if is_palindrome(word_input):
                st.write(f"{word_input} is a palindrome!")
            else:
                st.write(f"{word_input} is not a palindrome.")