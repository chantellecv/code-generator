import streamlit as st

def main():
    st.title("Sum Calculator")

    # Create two number inputs for user to input the integers
    num1 = st.number_input("Enter first number:", step=1, format='%d')
    num2 = st.number_input("Enter second number:", step=1, format='%d')

    # Button to calculate sum
    if st.button("Calculate Sum"):
        sum = num1 + num2
        # Display the result
        st.success(f"The sum of {num1} and {num2} is {sum}.")

if __name__ == "__main__":
    main()