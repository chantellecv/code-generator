import streamlit as st

st.title('Sum Calculator')

number1 = st.number_input('Enter the first number:')
number2 = st.number_input('Enter the second number:')

sum_result = number1 + number2

st.write(f'The sum of {number1} and {number2} is: {sum_result}')