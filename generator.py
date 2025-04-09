import streamlit as st

st.title("Factorial Calculator")

# Function to calculate the factorial of a number
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

# Main App
num = st.number_input("Enter a number to calculate its factorial:", min_value=0, step=1)
if st.button("Calculate"):
    result = factorial(num)
    st.success(f"The factorial of {num} is {result}")