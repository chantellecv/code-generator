import streamlit as st
import api_functions

def main():
    st.title("Number Sum App")

    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")

    if st.button("Sum"):
        result = api_functions.sum_numbers(num1, num2)
        st.write(f"The sum is: {result}")

if __name__ == "__main__":
    main()