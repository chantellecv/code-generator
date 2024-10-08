import streamlit as st

st.title("Even Number Checker")
st.write("Enter a number to check if it's even:")

num_input = st.number_input("Number:", min_value=0, key="num_input")

if st.button("Check", key="check_button"):
    if num_input % 2 == 0:
        st.write(f"{num_input} is an even number.")
    else:
        st.write(f"{num_input} is an odd number.")