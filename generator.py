import streamlit as st

st.title("Is it an odd number?")

num = st.number_input("Enter a number:", value=0, min_value=0, key="num_input")

if st.button("Check", key="check_button"):
    if num % 2 != 0:
        st.header("Yes, the number is odd!")
    else:
        st.header("No, the number is even!")