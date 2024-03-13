import streamlit as st

def calculate_difference(num1, num2):
    """Calculate and return the difference between two numbers."""
    return abs(num1 - num2)

# Setting up the Streamlit app
st.title('Integer Difference Calculator')

# Getting user input
num1 = st.number_input('Enter the first integer:', format='%d', step=1)
num2 = st.number_input('Enter the second integer:', format='%d', step=1)

# Button to calculate difference
if st.button('Calculate Difference'):
    difference = calculate_difference(num1, num2)
    st.success(f'The difference between {num1} and {num2} is {difference}.')