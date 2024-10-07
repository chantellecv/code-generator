import streamlit as st
import math

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Streamlit app
if __name__ == "__main__":
    st.title("Prime Number Checker")

    number_input = st.number_input("Enter a number to check for primality:")

    if st.button("Check"):
        if number_input < 1:
            st.write("Please enter a positive integer.")
        else:
            if is_prime(number_input):
                st.write(f"{number_input} is a prime number!")
            else:
                st.write(f"{number_input} is not a prime number.")