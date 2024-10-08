import streamlit as st
import math

# Define a function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Create a Streamlit app
st.title("Prime Number Checker")
st.header("Enter a number to check if it's prime:")

# Get the input number from the user
num = st.number_input("Number", min_value=1)

# Check if the number is prime
is_p = is_prime(num)

# Display the result
if is_p:
    st.write(f"{num} is a prime number.")
else:
    st.write(f"{num} is not a prime number.")

# Add a button to generate all prime numbers up to the input number
if st.button("Generate all prime numbers up to this number"):
    prime_numbers = []
    for i in range(2, num):
        if is_prime(i):
            prime_numbers.append(i)
    st.write("Prime numbers up to", num, "are:")
    st.write(prime_numbers)