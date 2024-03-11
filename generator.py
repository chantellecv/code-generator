import streamlit as st

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

st.title("Palindrome Checker")

user_input = st.text_input("Enter a string:")
if st.button("Check"):
    if is_palindrome(user_input):
        st.write(f"'{user_input}' is a palindrome!")
    else:
        st.write(f"'{user_input}' is not a palindrome.")