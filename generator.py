import streamlit as st

def sum_of_integers(num1, num2):
    return num1 + num2

st.title("Sum of Two Integers")
num1 = st.number_input("Enter the first integer:")
num2 = st.number_input("Enter the second integer:")

result = sum_of_integers(num1, num2)
st.write(f"The sum of {num1} and {num2} is: {result}")