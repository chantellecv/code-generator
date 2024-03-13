import streamlit as st

def is_prime(number):
    """Check if a number is a prime number."""
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Streamlit app UI
st.title('Prime Number Checker')
st.write('Enter a number to check if it is a prime number.')

# User input
number = st.number_input('Number', min_value=1, step=1)

if st.button('Check'):
    result = is_prime(number)
    if result:
        st.success(f"{number} is a prime number.")
    else:
        st.error(f"{number} is not a prime number.")