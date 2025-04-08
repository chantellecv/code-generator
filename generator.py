import streamlit as st

st.title("Number Subtraction App")

num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")

result = num1 - num2

st.write(f"The result of {num1} - {num2} is: {result}")