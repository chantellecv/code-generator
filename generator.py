import streamlit as st

# Title of the app
st.title('Difference Calculator')

# Getting user input
num1 = st.number_input('Enter the first integer:', value=0, format='%d')
num2 = st.number_input('Enter the second integer:', value=0, format='%d')

# Calculate the difference
difference = abs(num1 - num2)

# Display the result
st.write(f'The difference between {num1} and {num2} is {difference}.')