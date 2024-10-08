import streamlit as st
import math

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    sqrt_num = int(math.sqrt(num))
    for i in range(3, sqrt_num + 1, 2):
        if num % i == 0:
            return False
    return True

def app():
    st.title("Prime Number Finderrrrrr")
    numbers = st.text_input("Enter a list of numbers (separated by ','): ")
    if numbers:
        try:
            numbers = list(map(int, numbers.split(',')))
            prime_numbers = [num for num in numbers if is_prime(num)]
            st.write("Prime numbers are: ")
            st.write(prime_numbers)
        except ValueError:
            st.write("Invalid input. Please enter a list of integers separated by commas.")

if __name__ == '__main__':
    app()