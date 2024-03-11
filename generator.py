import streamlit as st

# Create a function to calculate the sum of even numbers in the list
def sum_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return sum(even_numbers)

# Streamlit app title and description
st.title('Sum of Even Numbers in a List')
st.write('This app takes a list of integers as input and returns the sum of all even numbers in the list.')

# User input of list of integers
numbers = st.text_input('Enter a list of integers separated by comma (,)', 'e.g. 1, 2, 3, 4, 5')

# Convert user input to a list of integers
numbers_list = [int(num) for num in numbers.split(',') if num.strip().isdigit()]

# Calculate and display the sum of even numbers in the list
if st.button('Calculate Sum of Even Numbers'):
    sum_even = sum_even_numbers(numbers_list)
    st.write(f'The sum of even numbers in the list {numbers_list} is: {sum_even}')