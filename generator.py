import streamlit as st

def determine_odd(num):
    if num % 2 != 0:
        return "Odd"
    else:
        return "Even"

st.title("Odd or Even?")
st.header("Enter a number:")

num = st.number_input("Number:")

if st.button("Check"):
    result = determine_odd(int(num))
    st.write(result)