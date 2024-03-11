import streamlit as st

st.title('Integer Sum Calculator')

# User input for the first integer
num1 = st.number_input('Enter the first integer:', value=0, step=1)

# User input for the second integer
num2 = st.number_input('Enter the second integer:', value=0, step=1)

# Calculate the sum of the two integers
result = num1 + num2

# Display the result
st.write(f'The sum of {num1} and {num2} is: {result}')