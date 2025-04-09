import streamlit as st

st.title('Simple Calculator App')

# Function to perform addition
def add_numbers(num1, num2):
    return num1 + num2

# Function to perform subtraction
def subtract_numbers(num1, num2):
    return num1 - num2

# Function to perform multiplication
def multiply_numbers(num1, num2):
    return num1 * num2

# Function to perform division
def divide_numbers(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2

operation = st.selectbox(
    "Select an operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")

if operation == "Addition":
    result = add_numbers(num1, num2)
elif operation == "Subtraction":
    result = subtract_numbers(num1, num2)
elif operation == "Multiplication":
    result = multiply_numbers(num1, num2)
elif operation == "Division":
    result = divide_numbers(num1, num2)

st.write(f"Result of {operation}: {result}")