# Import the Streamlit library
import streamlit as st

# Create a title for your app
st.title('Sum Calculator')

# Create input fields to input the integers
number1 = st.number_input('Enter first integer', value=0, format='%d')
number2 = st.number_input('Enter second integer', value=0, format='%d')

# Button to perform the sum
if st.button('Calculate Sum'):
    # Calculate the sum
    sum_result = number1 + number2
    
    # Display the result
    st.write('The sum is:', sum_result)