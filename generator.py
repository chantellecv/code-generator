import streamlit as st
import api_functions

def main():
    st.title("Anagram Checker")

    word1 = st.text_input("Enter the first word:")
    word2 = st.text_input("Enter the second word:")

    if st.button("Check"):
        result = api_functions.check_anagrams(word1, word2)
        st.write(f"{result}")

if __name__ == "__main__":
    main()

def check_anagrams(word1, word2):
    return sorted(word1) == sorted(word2)