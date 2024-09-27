import streamlit as st
import re

# Define a function to count the number of words in a sentence
def count_words(sentence):
    # Use regular expression to split the sentence into words
    words = re.split(r'\W+', sentence)
    # Return the count of words
    return len([word for word in words if word != ''])

# Create a Streamlit app
st.title("Word Counter")
st.header("Enter a sentence: ")

# Create a text input field for user input
user_input = st.text_input("")

# If the user has input a sentence, count the number of words
if user_input:
    word_count = count_words(user_input)
    st.write(f"The sentence contains {word_count} words.")