import streamlit as st

def sum_of_integers(num1, num2):
    return num1 + num2

st.title('Sum of Two Integers Calculator')

num1 = st.number_input('Enter the first integer:', step=1)
num2 = st.number_input('Enter the second integer:', step=1)

result = sum_of_integers(num1, num2)

st.write(f'The sum of {num1} and {num2} is: {result}')