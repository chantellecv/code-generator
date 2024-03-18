import streamlit as st

# Create a title and description for the app
st.title("Divisibility Checker")
st.write("Enter a number to check if it is divisible by 2.")

# User input for the number
number = st.number_input("Enter a number:")

# Check if the number is divisible by 2
if number % 2 == 0:
    st.write(f"{number} is divisible by 2")
else:
    st.write(f"{number} is not divisible by 2")