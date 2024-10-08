import streamlit as st
import string

def check_palindrome(word):
    word = word.lower().translate(str.maketrans('', '', string.punctuation)).replace(" ", "")
    return word == word[::-1]

st.title("Palindrome Checker")

if 'word_input' not in st.session_state:
    st.session_state.word_input = ''

st.header("Enter a word to check if it's a palindrome:")
word_input = st.text_input("Word:", key='word_input', value=st.session_state.word_input)

if st.button("Check_palindrome", key="check_palindrome_button"):
    result = check_palindrome(word_input)
    if result:
        st.session_state.word_input = ''
        st.write(f"'{word_input}' is a palindrome!")
    else:
        st.session_state.word_input = word_input
        st.write(f"'{word_input}' is not a palindrome.")