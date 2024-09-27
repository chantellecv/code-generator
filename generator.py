import streamlit as st
import math

def main():
    st.title("Is my number odd or even?")

    user_number = st.number_input("Enter a number:")

    try:
        user_number = float(user_number)
    except ValueError:
        st.error("Invalid input, please enter a number.")
        return

    result = "ODD" if math.floor(user_number) % 2 != 0 else "EVEN"

    st.header(f"The number {user_number} is {result}.")

if __name__ == "__main__":
    main()