import streamlit as st
import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True

st.title("Prime Number Checker")
st.write("Enter a number to check if it's prime:")

num_str = 'num_input'
num = st.number_input("Number:", min_value=1, key=num_str)

if st.button("Check", key=f"check_button"):
    if is_prime(int(num)):
        st.write(f"{num} is a prime number.")
    else:
        st.write(f"{num} is not a prime number.")