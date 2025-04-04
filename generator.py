import streamlit as st

def check_anagrams(word1, word2):
    return sorted(word1) == sorted(word2)

st.title("Anagram Checker")

word1 = st.text_input("Enter the first word:")
word2 = st.text_input("Enter the second word:")

if st.button("Check Anagrams"):
    if check_anagrams(word1, word2):
        st.write(f"{word1} and {word2} are anagrams!")
    else:
        st.write(f"{word1} and {word2} are not anagrams.")