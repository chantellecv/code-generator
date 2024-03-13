# Import Streamlit
import streamlit as st

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

# Streamlit app starts here
st.title('Prime Number Checker')

# User input
number = st.number_input('Enter a number', min_value=1, value=1, step=1)

# Button to check if the number is prime
if st.button('Check if Prime'):
    # Prime check
    if is_prime(number):
        st.success(f"{number} is a prime number.")
    else:
        st.error(f"{number} is not a prime number.")