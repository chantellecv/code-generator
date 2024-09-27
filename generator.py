Python
import streamlit as st
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

st.title("Is Prime Number")

num = st.number_input("Enter a number: ")

if st.button("Check"):
    result = is_prime(int(num))
    if result:
        st.write(f"{num} is a prime number.")
    else:
        st.write(f"{num} is not a prime number.")