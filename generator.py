import streamlit as st

st.title("Sum Calculator")

num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")

result = num1 + num2

st.write(f"The sum of {num1} and {num2} is: {result}")