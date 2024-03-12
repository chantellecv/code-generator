# Import the Streamlit library
import streamlit as st

# Function to check if a number is prime
def is_prime(number):
    """Return True if the number is prime, else return False."""
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Streamlit application starts here
def main():
    # App title
    st.title('Prime Number Checker')

    # User input to enter a number
    number = st.number_input('Enter a number', min_value=1, step=1)

    # Button to check if the number is prime
    if st.button('Check if prime'):
        if is_prime(number):
            st.success(f"{number} is a prime number!")
        else:
            st.error(f"{number} is not a prime number.")

# Call the main function to run the app
if __name__ == '__main__':
    main()