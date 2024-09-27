import streamlit as st
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

st.title("Prime Number Checkerrrrr")

num = st.number_input("Enter a number:", step=1)

if st.button("Check"):
    if is_prime(num):
        st.success(f"{num} is a prime number!")
    else:
        st.error(f"{num} is not a prime number.")

st.stop()