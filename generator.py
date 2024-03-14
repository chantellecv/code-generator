import streamlit as st

def main():
    # Set up the title of the app
    st.title('Sum Calculator')

    # Ask the user to input two numbers
    number1 = st.number_input('Enter first number', value=0, step=1)
    number2 = st.number_input('Enter second number', value=0, step=1)

    # Button to trigger the sum calculation
    if st.button('Calculate Sum'):
        sum_result = number1 + number2
        # Display the result of the addition
        st.write('The sum of', number1, 'and', number2, 'is:', sum_result)

if __name__ == '__main__':
    main()