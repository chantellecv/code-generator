import streamlit as st

# Function to check if the word is a palindrome
def is_palindrome(word):
    # Remove case sensitivity and spaces from the input
    word = word.replace(" ", "").lower()
    # Check if the word is equal to its reverse
    return word == word[::-1]

# Streamlit app interface
def main():
    # App title
    st.title("Palindrome Checker")

    # User input
    word = st.text_input("Enter a word to check if it's a palindrome:")

    # Button to check palindrome
    if st.button('Check'):
        if word:  # Check if the input is not empty
            if is_palindrome(word):
                st.success(f'"{word}" is a palindrome!')
            else:
                st.error(f'"{word}" is not a palindrome.')
        else:
            st.warning("Please enter a word to check.")

if __name__ == "__main__":
    main()