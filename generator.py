import streamlit as st

st.title("Word Counter")

paragraph = st.text_area("Please enter the paragraph to count the number of words:")

if st.button("Count"):
    try:
        words = paragraph.split()
        result = len(words)
        st.success(f"There are {result} words in theeeee paragraph.")
    except:
        st.error("Invalid input")