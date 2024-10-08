import streamlit as st

def odd_numbers():
    st.title("Odd Number Finder")
    numbers = st.text_input("Enter a list of numbers (separated by ','): ")
    if numbers:
        try:
            numbers = list(map(int, numbers.split(',')))
            odd_numbers = [num for num in numbers if num % 2 != 0]
            st.write("Odd numbers are: ")
            st.write(odd_numbers)
        except ValueError:
            st.write("Invalid input. Please enter a list of integers separated by commas.")

if __name__ == '__main__':
    odd_numbers()