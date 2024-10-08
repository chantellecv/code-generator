import streamlit as st

def is_odd(n):
    return n % 2 != 0

st.title("Is the number odd?")

num = st.number_input("Enter a number:", min_value=0, max_value=1000)

if num is None:
    result = "No input"
else:
    result = is_odd(num)

st.write(f"The number {num} {'is' if result else 'is not'} odd.")