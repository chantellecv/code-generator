import streamlit as st

def is_prime(number):
    """Function to determine if a number is a prime number."""
    # Handle the case of numbers less than 2 and number 2 itself
    if number < 2:
        return False
    if number == 2:
        return True
    # Check divisibility by numbers up to the square root of the number
    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0:
            return False
    return True

# Streamlit application starts here
st.title('Prime Number Checker')

# User inputs the number
number = st.number_input('Enter a number', min_value=1, step=1)

# Display the result
if st.button('Check if Prime'):
    if is_prime(number):
        st.success(f"{number} is a prime number.")
    else:
        st.error(f"{number} is not a prime number.")