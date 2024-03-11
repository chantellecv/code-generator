import streamlit as st

# Title of the Streamlit app
st.title("Character Counter App")

# Text input for user to enter a string
user_input = st.text_input("Enter a string:")

# Display the number of characters in the string entered by the user
if user_input:
    num_characters = len(user_input)
    st.write(f"The number of characters in the string: {num_characters}")