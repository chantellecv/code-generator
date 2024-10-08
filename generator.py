import streamlit as st
import string

def check_palindrome(word):
    word = word.lower().translate(str.maketrans('', '', string.punctuation)).replace(" ", "")
    return word == word[::-1]

st.title("Palindrome Checker")
st.header("Enter a word to check if it's a palindrome:")
word_input = st.text_input("Word:")
check_button = st.button("Check", key="check")

if check_button:
    if check_palindrome(word_input):
        st.write(f"'{word_input}' is a palindrome!")
    else:
        st.write(f"'{word_input}' is not a palindrome.")