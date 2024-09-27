import streamlit as st

def is_even(n):
    return n % 2 == 0

st.title("Even Number Checker")

num = st.number_input("Enter a number:", step=1)

if st.button("Check"):
    if is_even(num):
        st.success(f"{num} is an even number!")
    else:
        st.error(f"{num} is not an even number.")

st.stop()