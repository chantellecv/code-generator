Python
import streamlit as st
from st_code_formatter import format_code

def word_counter(text):
    return len(text.split())

st.title("Word Counter")

# Add a text box and a button to the app
text = st.text_area("Please enter the text to count the number of words:")
if st.button("Count"):
    try:
        result = word_counter(text)
        st.success(f"The number of words is: {result}")
    except:
        st.error("Invalid input")

# Format the code for better readability
st.code("