```python
import streamlit as st

st.title("Simple Game App")

option = st.selectbox(
    'Select a number:',
    ('1', '2', '3')
)

st.write('You selected:', option)

if option == '1':
    st.image("https://via.placeholder.com/150")
    st.write("Congratulations! You won!")
elif option == '2':
    st.image("https://via.placeholder.com/150")
    st.write("Sorry, you lost!")
elif option == '3':
    st.image("https://via.placeholder.com/150")
    st.write("Try again!")
```