import streamlit as st

st.title('Calculator App')

num1 = st.number_input('Enter the first number:')
num2 = st.number_input('Enter the second number:')

operation = st.selectbox('Select operation', ['Addition', 'Subtraction', 'Multiplication', 'Division'])

result = 0

if operation == 'Addition':
    result = num1 + num2
elif operation == 'Subtraction':
    result = num1 - num2
elif operation == 'Multiplication':
    result = num1 * num2
elif operation == 'Division':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Division by zero is undefined"

st.write('Result:', result)