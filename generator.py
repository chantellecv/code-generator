import streamlit as st
import math

# Create a Streamlit app
st.title("Prime Number Checker")

# Create a text box to input a number
num = st.number_input("Enter a number:")

# Create a button to check if the number is prime
if st.button("Check"):
    if num < 2:
        result = "Not a prime number"
    else:
        if math.sqrt(num) % 1 == 0:
            result = "Not a prime number"
        else:
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    result = "Not a prime number"
                    break
            else:
                result = "Prime number"

    # Display the result
    st.write(f"{num} {result}")