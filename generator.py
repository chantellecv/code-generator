import streamlit as st

# Create a title for the app
st.title("Number Divisibility Checker")

# Create a text input for the user to enter a number
number = st.number_input("Enter a number:")

# Check if the number is divisible by 3
if number % 3 == 0:
    st.write(f"{number} is divisible by 3")
else:
    st.write(f"{number} is not divisible by 3")