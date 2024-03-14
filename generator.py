import streamlit as st

# Title of the app
st.title('D Letter Detector')

# Text input for the word
word = st.text_input("Enter a word:", "")

# Function to check for 'd' in the word
def contains_d(word):
    return 'd' in word.lower()

# When a word is entered
if word:
    # Check if the word contains 'd'
    if contains_d(word):
        st.success("Yes! The word contains the letter 'd'.")
    else:
        st.error("No, the word does not contain the letter 'd'.")