import streamlit as st

# Create a Streamlit app
st.title("Odd Number Checker")

# Get the input number from the user
number_input = st.text_input("Enter a number")

# Check if the number is odd
if number_input:
    num = int(number_input)
    if num % 2 != 0:
        st.write(f"{num} is an odd number.")
    else:
        st.write(f"{num} is an even number.")
else:
    st.write("Please enter a number.")