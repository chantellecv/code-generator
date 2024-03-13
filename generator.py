import streamlit as st

# Streamlit app title
st.title('Difference Calculator')

# Get user input for two integers
num1 = st.number_input('Enter first integer:', value=0, format='%d')
num2 = st.number_input('Enter second integer:', value=0, format='%d')

# Calculate the difference
difference = num1 - num2

# Display the difference
st.write('The difference between ', num1, ' and ', num2, ' is ', difference)