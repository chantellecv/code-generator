import streamlit as st

# Create a Streamlit app
st.title("Odd Number Checker")

# Get the input number from the user
number_input = st.number_input("Enter a number", value=0, key="odd_number_input")

# Check if the number is odd
if number_input % 2 != 0:
    st.write(f"{number_input} is an odd number.")
else:
    st.write(f"{number_input} is an even number.")