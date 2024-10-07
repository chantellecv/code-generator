import streamlit as st
import enchant

# Function to check if a word is a palindrome
def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

# Function to check if a word is valid
def is_valid(word):
    d = enchant.Dict("en_US")
    return d.check(word)

# Streamlit app
if __name__ == "__main__":
    st.title("Palindrome Checker")

    word_input = st.text_input("Enter a word to check for palindrome:")

    if st.button("Check"):
        if not word_input:
            st.write("Please enter a word to check.")
        else:
            if is_valid(word_input):
                if is_palindrome(word_input):
                    st.write(f"'{word_input}' is a palindrome!")
                else:
                    st.write(f"'{word_input}' is not a palindrome.")
            else:
                st.write(f"'{word_input}' is not a valid English word.")