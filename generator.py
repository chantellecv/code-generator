import streamlit as st

def calculate_sum():
    numbers_input = st.text_input("Enter numbers separated by commasss", value="")
    if st.button("Submit"):
        try:
            numbers_list = [float(x) for x in numbers_input.split(',')]
            result = sum(numbers_list)
            st.header("Result")
            st.write(f"The sum of the numbers is: {result}")
        except ValueError:
            st.error("Invalid input. Please enter numbers separated by commas.")

if __name__ == "__main__":
    calculate_sum()