import streamlit as st

# Calculator app title
st.title('Basic Calculator App')

# Input numbers
number1 = st.number_input("Enter first number", format="%f")
number2 = st.number_input("Enter second number", format="%f")

# Operation selection
operation = st.selectbox("Choose an operation", ['Add', 'Subtract', 'Multiply', 'Divide'])

# Function to calculate result
def calculate(number1, number2, operation):
    if operation == 'Add':
        return number1 + number2
    elif operation == 'Subtract':
        return number1 - number2
    elif operation == 'Multiply':
        return number1 * number2
    elif operation == 'Divide':
        if number2 == 0:
            return "Error! Division by zero."
        else:
            return number1 / number2

# Display result
if st.button('Calculate'):
    result = calculate(number1, number2, operation)
    st.success(f"Result: {result}")

# Note on division by zero
if operation == 'Divide':
    st.write("Note: Selecting 'Divide' with second number as 0 will result in an error.")