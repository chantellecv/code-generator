Python
import streamlit as st

def word_counter(text):
    return len(text.split())

st.title("Word Counter")

paragraph = st.text_area("Please enter the paragraph to count the number of words:")

if st.button("Count"):
    try:
        result = word_counter(paragraph)
        st.success(f"The number of words is: {result}")
    except:
        st.error("Invalid input")