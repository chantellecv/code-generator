import streamlit as st

def even_numbers(app):
    st.title("Even Number Finder")
    numbers = st.text_input("Enter a list of numbers (separated by ','): ")
    if numbers:
        try:
            numbers = list(map(int, numbers.split(',')))
            even_numbers = [num for num in numbers if num % 2 == 0]
            st.write("Even numbers are: ")
            st.write(even_numbers)
        except ValueError:
            st.write("Invalid input. Please enter a list of integers separated by commas.")

if __name__ == '__main__':
    even_numbers()