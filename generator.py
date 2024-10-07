import streamlit as st

def main():
    # Set the title of the app
    st.title("Difference of Two Numbers")

    # Add a header to the app
    st.header("Enter two numbers to calculate the difference:")

    # Create a text input for the first number
    num1 = st.number_input("Enter the first number:", value=0.0)

    # Create a text input for the second number
    num2 = st.number_input("Enter the second number:", value=0.0)

    # Create a button to trigger the calculation
    if st.button("Calculate"):
        if num2 > num1:
            result = num2 - num1
            st.markdown(f"The difference between {num1} and {num2} is: **{result}**")
        elif num1 > num2:
            result = num1 - num2
            st.markdown(f"The difference between {num2} and {num1} is: **{result}**")
        else:
            st.markdown(f"The difference between {num1} and {num2} is: **0**")

if __name__ == "__main__":
    main()