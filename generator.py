import streamlit as st

def main():
    # App title
    st.title('Sum Calculator')

    # Getting user input for the two numbers
    num1 = st.number_input('Enter first number:', min_value=None, max_value=None, value=0, step=1)
    num2 = st.number_input('Enter second number:', min_value=None, max_value=None, value=0, step=1)

    # User action to perform the sum
    if st.button('Calculate Sum'):
        result = num1 + num2
        st.write('The sum of {} and {} is: {}'.format(num1, num2, result))

if __name__ == '__main__':
    main()