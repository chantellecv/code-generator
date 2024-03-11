import streamlit as st

# Title of the Streamlit app
st.title("Sum of Two Integers")

# Input for the first integer
num1 = st.number_input("Enter the first integer:")

# Input for the second integer
num2 = st.number_input("Enter the second integer:")

# Calculate the sum of the two integers
sum_result = num1 + num2

# Display the result
st.write(f"The sum of {num1} and {num2} is: {sum_result}")