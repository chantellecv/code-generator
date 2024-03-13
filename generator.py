import streamlit as st

# Streamlit app title
st.title('Difference Calculator')

# User inputs
num1 = st.number_input('Enter first integer:', format='%d', step=1)
num2 = st.number_input('Enter second integer:', format='%d', step=1)

# Button to calculate difference
if st.button('Calculate Difference'):
    difference = num1 - num2
    # Displaying the result
    st.write(f'The difference between {num1} and {num2} is {difference}.')