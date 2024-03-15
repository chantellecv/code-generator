import streamlit as st

# Title for your app
st.title('Check the letter G in a word')

# User input
word = st.text_input('Enter your word')

# Function to check 'g' or 'G' in the word
def check_g(word):
    if 'g' in word.lower():
        return "Yes, the word contains the letter 'g'."
    else:
        return "No, the word does not contain the letter 'g'."

# Only display the button and process the input if a word is entered
if word:
    # Button to check the word
    if st.button('Check for G'):
        # Display the result
        st.write(check_g(word))