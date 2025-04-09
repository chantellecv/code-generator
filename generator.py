import streamlit as st

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

st.title('Factorial Calculator')

number = st.number_input('Enter a number:', min_value=0, step=1)
if st.button('Calculate Factorial'):
    result = factorial(int(number))
    st.write(f'The factorial of {number} is {result}')