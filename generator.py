import streamlit as st
import math

st.title("Product Calculator")

st.subheader("Enter the numbers separated by space")

# Create a text input for the user to enter numbers
numbers = st.text_input("Enter numbers", key="numbers")

if numbers:
    numbers = [int(x) for x in numbers.split()]
    product = math.prod(numbers)
    st.write("The product of the numbers is:", product)
else:
    st.write("Please enter numbers separated by space.")