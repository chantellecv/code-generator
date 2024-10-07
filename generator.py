import streamlit as st

# Set the title of the app
st.title("Number Sum Calculator")

# Ask the user to enter the first number
num1 = st.number_input("Enter the first number:")

# Ask the user to enter the second number
num2 = st.number_input("Enter the second number:")

# Calculate the sum
if st.button("Calculate"):
    sum = num1 + num2
    st.header("Result")
    st.write("The sum of the two numbers is: ", sum)