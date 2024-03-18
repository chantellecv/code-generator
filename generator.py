import streamlit as st

def main():
    st.title("Number Divisibility Checker")

    number = st.number_input("Enter a number:", step=1)

    if number % 15 == 0:
        st.write(f"{number} is divisible by 15")
        st.write("YES IT WORKS")
    else:
        st.write(f"{number} is not divisible by 15")

if __name__ == '__main__':
    main()