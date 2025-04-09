import streamlit as st

st.title('Simple Calculator')

num1 = st.number_input('Enter the first number:')
num2 = st.number_input('Enter the second number:')

operation = st.selectbox('Select an operation', ['Addition', 'Subtraction', 'Multiplication', 'Division'])

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
        st.warning("Division by zero is not allowed. Please enter a non-zero value for the second number.")

st.write(f'Result: {result}')