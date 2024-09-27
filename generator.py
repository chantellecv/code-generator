import streamlit as st
import math

st.title("Odd Number Checker")

num = st.number_input("Enter a number:", step=1)

if st.button("Check"):
    if num % 2 != 0:
        st.success(f"{num} is an odd number!")
    else:
        st.error(f"{num} is not an odd number.")

    # Add an additional check for perfect squares
    num_sqrt = math.isqrt(num)
    if num_sqrt * num_sqrt == num:
        st.warning(f"{num} is a perfect square!")

st.stop()