import streamlit as st

# Title of the app
st.title('Sum Calculator')

# Input fields for user to enter two numbers
num1 = st.number_input('Enter the first number:')
num2 = st.number_input('Enter the second number:')

# Function to calculate the sum of two numbers
def calculate_sum(num1, num2):
    return num1 + num2

# Button to calculate the sum
if st.button('Calculate Sum'):
    result = calculate_sum(num1, num2)
    st.success(f'The sum of {num1} and {num2} is: {result}')