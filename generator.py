# Importing necessary library
import streamlit as st

# Function to check if the number is prime
def is_prime(n):
    """Check if a number is a prime number."""
    # Check for edge cases
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Streamlit app
def main():
    # App title
    st.title('Prime Number Checker')
    
    # Getting user input
    number = st.number_input('Enter a number', min_value=0, format="%d")
    
    # Displaying result
    if st.button('Check'):
        if is_prime(number):
            st.success(f"{number} is a prime number!")
        else:
            st.error(f"{number} is not a prime number.")

if __name__ == "__main__":
    main()