import streamlit as st

# Title for the app
st.title('Sum Calculator')

# Getting user inputs
number1 = st.number_input('Enter first integer:', format='%d', key='num1')
number2 = st.number_input('Enter second integer:', format='%d', key='num2')

# Button to calculate sum
if st.button('Calculate Sum'):
    sum = number1 + number2
    st.write('The sum of', number1, 'and', number2, 'is:', sum)