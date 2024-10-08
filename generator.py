import streamlit as st
import math

st.title("Product Calculator")

st.subheader("Enter the numbers separated by space")

# Create a text input for the user to enter numbers
numbers_key = "user_numbers"
numbers_input = st.text_input(numbers_key)

# Split the input string into a list of numbers
if numbers_input:
    numbers = [int(x) for x in numbers_input.split()]
    # Calculate the product of the numbers
    product = math.prod(numbers)
    # Display the result
    st.write("The product of the numbers is:", product)
else:
    st.write("Please enter numbers separated by space.")