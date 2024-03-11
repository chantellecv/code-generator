python
import streamlit as st

# Title of the Streamlit app
st.title('Integer Sum Calculator')

# Input fields for the user to enter two integers
num1 = st.number_input('Enter the first integer:', value=0)
num2 = st.number_input('Enter the second integer:', value=0)

# Calculate the sum of the two integers
result = num1 + num2

# Display the result
st.write(f'The sum of {num1} and {num2} is: {result}')
