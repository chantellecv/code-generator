# Import necessary libraries
import streamlit as st

# Title of the web app
st.title("Integer Difference Calculator")

# Input integer values from the user
num1 = st.number_input("Enter the first integer:")
num2 = st.number_input("Enter the second integer:")

# Calculate the difference between the two integers
difference = num1 - num2

# Display the difference to the user
st.write(f"The difference between {num1} and {num2} is: {difference}")