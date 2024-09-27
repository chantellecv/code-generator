import streamlit as st

def is_odd(n):
    return n % 2 != 0

st.title("Odd Number Checker")

num = st.number_input("Enter a number:", step=1)

if st.button("Check"):
    if is_odd(num):
        st.success(f"{num} is an odd number!")
    else:
        st.error(f"{num} is not an odd number.")

st.stop()