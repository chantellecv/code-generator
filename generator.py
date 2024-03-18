import streamlit as st

def check_for_k(word):
    """Function to check if the word contains the letter 'k'."""
    return 'k' in word

# Setting up the Streamlit app
st.title('Check if a word contains the letter "k"')

# User input
user_input = st.text_input("Enter a word to check:")

# Submit button
if st.button('Check'):
    if check_for_k(user_input):
        st.success(f"The word '{user_input}' contains the letter 'k'.")
    else:
        st.error(f"The word '{user_input}' does not contain the letter 'k'.")