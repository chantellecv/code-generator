import streamlit as st

def check_letter_j(word):
    """Check if the word contains the letter 'j'."""
    return 'j' in word.lower()

# Streamlit app UI
st.title("Check for the letter 'j' in a word")

# User input
user_word = st.text_input("Enter a word:")

if user_word:
    # Check if the submitted word contains the letter 'j'
    contains_j = check_letter_j(user_word)
    
    # Display the result
    if contains_j:
        st.write(f"The word '{user_word}' contains the letter 'j'.")
    else:
        st.write(f"The word '{user_word}' does not contain the letter 'j'.")