import streamlit as st

st.title('Number Addition App')

num1 = st.number_input('Enter first number:')
num2 = st.number_input('Enter second number:')

result = num1 + num2

st.write('The result is:', result)