import streamlit as st

def calculate_sum(num1, num2):
    return num1 + num2

def main():
    st.title("Sum Calculator")

    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")

    sum_result = calculate_sum(num1, num2)

    st.write("The sum of", num1, "and", num2, "is", sum_result)

if __name__ == "__main__":
    main()