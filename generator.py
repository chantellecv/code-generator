import streamlit as st

# Create a Streamlit app
st.title("Odd Number Checker")

# Create a unique key for the number input
key = "number_input"

# Get the input number from the user
num = st.number_input("Number", min_value=0, key=key)

# Check if the number is odd
if num % 2 != 0:
    st.write(f"{num} is an odd number.")
else:
    st.write(f"{num} is an even number.")