import streamlit as st

st.title("Number Multiplier App")

number1 = st.number_input("Enter the first number:")
number2 = st.number_input("Enter the second number:")

result = number1 * number2

st.write(f"The result of multiplying {number1} and {number2} is: {result}")