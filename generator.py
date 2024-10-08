import streamlit as st

# Create a Streamlit app
st.title("Even Number Checker")

# Create a text input for the number
number_input = st.text_input(label="Enter a number", key="number_input")

# Check if the input is not empty
if number_input:
    # Convert the input string to an integer
    try:
        number = int(number_input)
    except ValueError:
        st.write("Invalid input. Please enter a whole number.")

    # Check if the number is even
    if number % 2 == 0:
        st.write(f"{number} is an even number.")
    else:
        st.write(f"{number} is an odd number.")
else:
    st.write("Please enter a number.")