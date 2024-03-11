Generated code based on prompt: Sure! Here is the Python code for a Streamlit app that calculates the sum of two integers:

```python
import streamlit as st

st.title('Sum of Two Integers Calculator')

# Input fields for the user to input the integers
num1 = st.number_input('Enter the first integer:', value=0)
num2 = st.number_input('Enter the second integer:', value=0)

# Calculate the sum of the two integers
result = num1 + num2

# Display the result to the user
st.write(f'The sum of {num1} and {num2} is: {result}')
```

You can copy and paste this code into a Python script and run it using Streamlit to create a web app that calculates the sum of two integers.')