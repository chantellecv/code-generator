import streamlit as st

def is_even(n):
    return n % 2 == 0

st.title("Is the number even?")

num = st.number_input("Enter a number:")

if st.button("Check"):
    result = is_even(num)
    st.write(f"The number {num} is {'even' if result else 'odd'}")