import streamlit as st

st.title("Odd Number Checker")

num = st.number_input("Enter a number:", step=1)

if st.button("Check"):
    if num % 2 != 0:
        st.success(f"YESSSSS{num} is an odd number!")
    else:
        st.error(f"NOOOO {num} is not an odd number.")

st.stop()