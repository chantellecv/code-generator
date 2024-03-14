import streamlit as st

def calculate_sum(a, b, c):
    return a + b + c

def main():
    st.title("Sum of Three Integers Calculator")

    # Creating three columns to input the integer values
    col1, col2, col3 = st.columns(3)
    with col1:
        num1 = st.number_input("Enter first number:", format="%d")
    with col2:
        num2 = st.number_input("Enter second number:", format="%d")
    with col3:
        num3 = st.number_input("Enter third number:", format="%d")

    # Button to calculate the sum
    if st.button("Calculate Sum"):
        result = calculate_sum(num1, num2, num3)
        st.success(f"The sum of {num1}, {num2}, and {num3} is: {result}")

if __name__ == "__main__":
    main()