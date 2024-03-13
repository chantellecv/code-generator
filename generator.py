import streamlit as st

# App title
st.title('Sum Calculator')

# Get user input for the two numbers
num1 = st.number_input('Enter first number', format='%d')
num2 = st.number_input('Enter second number', format='%d')

# Button to perform the calculation
if st.button('Calculate Sum'):
    # Perform the sum
    result = num1 + num2
    
    # Display the result
    st.write('The sum of', num1, 'and', num2, 'is:', result)