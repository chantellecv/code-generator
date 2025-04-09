import streamlit as st

# Function to calculate factorial
def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

# Streamlit app layout
st.title('Factorial Calculator')
number = st.number_input('Enter a number:', value=0, step=1)
if st.button('Calculate Factorial'):
    result = calculate_factorial(int(number))
    st.write(f'The factorial of {number} is {result}')