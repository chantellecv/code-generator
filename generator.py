# Import Streamlit
import streamlit as st

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Streamlit user interface
def main():
    # Set up the web app title
    st.title("Prime Number Checker")
    
    # User input
    number = st.number_input("Enter a number", min_value=2, step=1)
    
    if number:
        # Check if the user input is a prime number or not
        if is_prime(number):
            st.success(f"{number} is a prime number!")
        else:
            st.error(f"{number} is not a prime number.")

# Entry point of the Streamlit app
if __name__ == "__main__":
    main()