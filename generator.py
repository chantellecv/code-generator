import streamlit as st

# Title of the app
st.title('Sum Calculator')

# Integer inputs
num1 = st.number_input('Enter first integer:', value=0, format='%d')
num2 = st.number_input('Enter second integer:', value=0, format='%d')

# Calculate button
if st.button('Calculate Sum'):
    sum_result = num1 + num2
    st.write(f"The sum of {num1} and {num2} is {sum_result}")