import streamlit as st

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Streamlit app starts here
st.title('Prime Number Checker')

# User input
number = st.number_input("Enter a number", min_value=1, step=1)

if number:
    # Call the function with the user input
    result = is_prime(number)
    
    # Display the result
    if result:
        st.success(f"{number} is a prime number.")
    else:
        st.error(f"{number} is not a prime number.")

# Run your app
# To run this Streamlit app, save the code in a file (e.g., prime_checker.py)
# and run it using Streamlit. Use the following command in your terminal or command prompt:
# streamlit run prime_checker.py