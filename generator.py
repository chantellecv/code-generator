import streamlit as st

def app():
    st.title("Is the number even?")
    number = st.number_input("Enter a number: ")

    if number % 2 == 0:
        result = "Yes, the number is even"
    else:
        result = "No, the number is odd"

    st.write(f"{number} is {result}")

if __name__ == "__main__":
    app()