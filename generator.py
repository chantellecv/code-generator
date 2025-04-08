import streamlit as st

st.title("Number Addition App")

num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")

result = num1 + num2

st.write("The sum of the two numbers is:", result)