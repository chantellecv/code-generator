# Import the Streamlit library
import streamlit as st

# Create the title for your app
st.title('Sum of Two Integers Calculator')

# Create input fields for the user to enter the two integers
num1 = st.number_input('Enter the first integer', value=0, format='%d')
num2 = st.number_input('Enter the second integer', value=0, format='%d')

# Button to perform the addition
if st.button('Calculate Sum'):
    # Calculate the sum
    result = num1 + num2
    
    # Display the result
    st.write('The sum of', num1, 'and', num2, 'is:', result)