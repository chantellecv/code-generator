import streamlit as st

st.title("Number Difference Calculator")

# User input
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")

# Calculate the difference
difference = num1 - num2

# Display the difference
st.write(f"The difference between the two numbers is: {difference}")