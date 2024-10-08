import streamlit as st
def app():
    st.title("Is the number odd?")
    number = st.number_input("Enter a number: ")

    if number % 2 != 0:
        st.write(f"{number} is odd")
    else:
        st.write(f"{number} is even")

if __name__ == "__main__":
    app()