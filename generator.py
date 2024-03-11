import streamlit as st

def sum_of_even_numbers(lst):
    result = 0
    for num in lst:
        if num % 2 == 0:
            result += num
    return result

def main():
    st.title('Sum of Even Numbers App')
    
    input_numbers = st.text_input('Enter a list of integers separated by commas (e.g., 1,2,3,4):')
    
    if input_numbers:
        numbers_list = [int(num) for num in input_numbers.split(',')]
        result = sum_of_even_numbers(numbers_list)
        st.write('List of numbers:', numbers_list)
        st.write('Sum of even numbers:', result)

if __name__ == '__main__':
    main()