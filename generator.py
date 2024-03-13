import streamlit as st

def is_prime(number):
    """Check if a number is a prime number."""
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Streamlit app layout
st.title("Prime Number Checker")

# Input for the user to enter a number
number = st.number_input("Enter a number", min_value=1, step=1, format='%d')

# Button to check if the number is prime
if st.button('Check if Prime'):
    # Using the is_prime function to check if the number is prime
    prime_status = is_prime(number)
    
    # Displaying the result
    if prime_status:
        st.success(f"{number} is a prime number.")
    else:
        st.error(f"{number} is not a prime number.")