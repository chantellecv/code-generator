import streamlit as st

def main():
    st.title('Sum Calculator')

    # Getting the user input
    num1 = st.number_input('Enter first integer:', value=0, format='%d')
    num2 = st.number_input('Enter second integer:', value=0, format='%d')

    # Button to perform addition
    if st.button('Calculate Sum'):
        sum_result = num1 + num2
        st.success(f'The sum of {num1} and {num2} is {sum_result}')

if __name__ == '__main__':
    main()