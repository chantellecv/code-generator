python
import streamlit as st

def is_palindrome(word):
    return word.lower() == word.lower()[::-1]

def main():
    st.title('Palindrome Checker')

    word1 = st.text_input('Enter the first word:')
    word2 = st.text_input('Enter the second word:')

    if st.button('Check Palindrome'):
        if is_palindrome(word1) and is_palindrome(word2):
            st.write(f'Both "{word1}" and "{word2}" are palindromes!')
        elif is_palindrome(word1):
            st.write(f'Only "{word1}" is a palindrome.')
        elif is_palindrome(word2):
            st.write(f'Only "{word2}" is a palindrome.')
        else:
            st.write('Neither of the words is a palindrome.')

if __name__ == '__main__':
    main()