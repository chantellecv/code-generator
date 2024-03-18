import streamlit as st

def check_for_letter_l(word):
    """Function to check if the word contains the letter 'l'."""
    return 'l' in word.lower()

# Setting up the Streamlit app
st.title('Check if a word contains the letter "l"')

# User input
user_input = st.text_input("Enter a word to check:")

# Submit button
if st.button('Check'):
    if check_for_letter_l(user_input):
        st.success(f"The word '{user_input}' contains the letter 'l'.")
    else:
        st.error(f"The word '{user_input}' does not contain the letter 'l'.")