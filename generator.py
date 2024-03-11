python
import streamlit as st

# Page title
st.title('Sum of Two Integers')

# User input for two integers
num1 = st.number_input('Enter the first integer:', value=0)
num2 = st.number_input('Enter the second integer:', value=0)

# Calculate the sum
sum = num1 + num2

# Display the sum
st.write(f'The sum of {num1} and {num2} is: {sum}')
