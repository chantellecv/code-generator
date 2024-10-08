import streamlit as st
def app():
    st.title("Is the number odd?")
    number = st.number_input("Enter a number: ")

    while True:
        if number % 2 != 0:
            st.write(f"{number} is odd")
            break
        else:
            st.write(f"{number} is not odd, please try again.")
            number = int(st.text_input("Enter a new number: ", value=str(number)))

    st.write("Experiment complete, thank you!")
if __name__ == "__main__":
    app()