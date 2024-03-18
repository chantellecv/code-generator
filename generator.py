import streamlit as st

# Create a title for the app
st.title("Number Divisibility Checker")

# Create a text input for the user to enter a number
number = st.number_input("Enter a number:")

# Check if the number is divisible by 2
if number % 2 == 0:
    st.write(f"{number} is divisible by 2")
else:
    st.write(f"{number} is not divisible by 2")