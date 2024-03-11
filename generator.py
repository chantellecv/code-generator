Here is a sample code to determine the sum of two integers using a Streamlit app:

```python
import streamlit as st

def sum_of_integers(num1, num2):
    return num1 + num2

# Streamlit app layout
st.title('Sum of Two Integers')
st.write('Enter two integers to calculate their sum:')
num1 = st.number_input('Enter the first integer:', step=1)
num2 = st.number_input('Enter the second integer:', step=1)

if st.button('Calculate Sum'):
    sum_result = sum_of_integers(num1, num2)
    st.write(f'The sum of {num1} and {num2} is: {sum_result}')
```

You can copy and paste this code into a Python script, save it as `sum_of_integers_app.py`, and run it using Streamlit to create an app where you can calculate the sum of two integers.