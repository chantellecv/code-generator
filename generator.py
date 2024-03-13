# Import Streamlit
import streamlit as st

# Function to check if the number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Streamlit application start
def main():
    # Add a title
    st.title('Prime Number Checker')
    
    # User input
    number = st.number_input('Enter a number', min_value=1, step=1)
    
    # Button to check the number
    if st.button('Check if Prime'):
        result = is_prime(number)
        if result:
            st.success(f"{number} is a prime number!")
        else:
            st.error(f"{number} is not a prime number.")

if __name__ == "__main__":
    main()