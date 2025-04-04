python
import streamlit as st

def check_anagrams(word1, word2):
    if sorted(word1.lower()) == sorted(word2.lower()):
        return True
    else:
        return False

st.title('Anagram Checker')

word1 = st.text_input('Enter the first word:')
word2 = st.text_input('Enter the second word:')
result = check_anagrams(word1, word2)

if st.button('Check Anagrams'):
    if result:
        st.write(f'{word1} and {word2} are anagrams!')
    else:
        st.write(f'{word1} and {word2} are not anagrams.')