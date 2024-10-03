import streamlit as st
from function import sum_numbers  # Assuming you define the sum_numbers function in the function.py file

st.header('Sum Calculator')

num1 = st.number_input('Enter the first number:', min_value=0.0)
num2 = st.number_input('Enter the second number:', min_value=0.0)

if st.button('Calculate Sum'):
    result = sum_numbers(num1, num2)
    st.header('Result')
    st.write(result)