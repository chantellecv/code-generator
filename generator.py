import streamlit as st

def is_odd(num):
    if num % 2 != 0:
        return "odd"
    else:
        return "even"

st.title("Is the number odd?")
num = st.number_input("Enter a number:", min_value=0, value=0)

if st.button("Check if number is odd"):
    result = is_odd(int(num))
    st.write(f"{num} is a {result} number.")