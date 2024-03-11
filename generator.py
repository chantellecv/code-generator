# Import required library
import streamlit as st

# Function to calculate the sum of two integers
def sum_of_integers(num1, num2):
    return num1 + num2

# Streamlit app
def main():
    st.title('Sum of Two Integers Calculator')

    # User input for the two integers
    num1 = st.number_input('Enter the first integer:')
    num2 = st.number_input('Enter the second integer:')

    # Calculate and display the sum
    result = sum_of_integers(num1, num2)
    st.write('The sum of the two integers is: ', result)

if __name__ == '__main__':
    main()