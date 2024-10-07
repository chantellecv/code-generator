import streamlit as st

def calculate_difference(num1, num2):
    if num1 >= num2:
        return num1 - num2
    else:
        return num2 - num1

def main():
    st.title("Difference Calculator")

    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")

    difference_result = calculate_difference(num1, num2)

    st.write("The difference between", num1, "and", num2, "is", difference_result)

if __name__ == "__main__":
    main()