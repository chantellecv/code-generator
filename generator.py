import streamlit as st

# App title
st.title('Does the word contain "b"?')

# Text input for the user to enter a word
word = st.text_input('Enter a word:').lower()

# Function to check if 'b' is in the word
def check_b(word):
    if 'b' in word:
        return True
    else:
        return False

# Button to check the word
if st.button('Check the word'):
    # Using the function to check the word
    result = check_b(word)
    
    # Displaying the result
    if result:
        st.success('Yes, the word contains "b".')
    else:
        st.error('No, the word does not contain "b".')

# The Streamlit command to run the app. 
# This should be executed in your terminal, not in the script.
# streamlit run app.py