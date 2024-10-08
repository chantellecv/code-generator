import streamlit as st
import math

def prime_number(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = math.isqrt(n)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

st.title("Prime Number Checker")

n = st.number_input("Enter a number:", value=1, step=1)

if st.button("Check"):
    if prime_number(n):
        st.write(f"{n} is a prime number")
    else:
        st.write(f"{n} is not a prime number")