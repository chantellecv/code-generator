import streamlit as st

def is_odd(n):
    return n % 2 != 0

st.title("Is the number odd?")

num = st.number_input("Enter a number:")

if st.button("Check"):
    result = is_odd(num)
    st.write(f"The number {num} is {'odd' if result else 'even'}")