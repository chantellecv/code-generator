# Import Streamlit
import streamlit as st

# Prime number checker function
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Streamlit app interface
st.title("Prime Number Checker")

# Input from user
number = st.number_input("Enter a number", min_value=1, step=1)

# Button to check the number
if st.button("Check if prime"):
    # Use the prime check function
    result = is_prime(number)
    
    # Display the result
    if result:
        st.success(f"{number} is a prime number!")
    else:
        st.error(f"{number} is not a prime number.")