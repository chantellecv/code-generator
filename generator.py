import streamlit as st

# Title of the Streamlit app
st.title('Integer Sum Calculator')

# Get user input for the two integers
num1 = st.number_input('Enter the first integer:', value=0)
num2 = st.number_input('Enter the second integer:', value=0)

# Calculate the sum of the two integers
sum_result = num1 + num2

# Display the sum to the user
st.write(f'The sum of {num1} and {num2} is: {sum_result}')