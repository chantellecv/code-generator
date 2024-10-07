import streamlit as st

def main():
    # Set the title of the app
    st.title("Sum of Two Numbers")

    # Add a header to the app
    st.header("Enter two numbers to calculate the sum:")

    # Create a text input for the first number
    num1 = st.number_input("Enter the first number:", value=0.0)

    # Create a text input for the second number
    num2 = st.number_input("Enter the second number:", value=0.0)

    # Create a button to trigger the calculation
    if st.button("Calculate"):
        result = num1 + num2
        st.markdown(f"The sum of {num1} and {num2} is: **{result}**")

if __name__ == "__main__":
    main()