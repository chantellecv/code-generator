import streamlit as st

def is_palindrome(s):
    return s == s[::-1]

st.title('Palindrome Checker')

string1 = st.text_input('Enter the first string:')
string2 = st.text_input('Enter the second string:')

if st.button('Check Palindrome'):
    if is_palindrome(string1) and is_palindrome(string2):
        st.write('Both strings are palindromes!')
    elif is_palindrome(string1):
        st.write('The first string is a palindrome, but the second string is not.')
    elif is_palindrome(string2):
        st.write('The second string is a palindrome, but the first string is not.')
    else:
        st.write('Neither string is a palindrome.')