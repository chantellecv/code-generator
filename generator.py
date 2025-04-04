python
import streamlit as st

def check_anagram(word1, word2):
    # Remove spaces and convert to lowercase
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    
    # Check if both words have the same characters
    return sorted(word1) == sorted(word2)

# Streamlit UI
st.title("Anagram Checker")
st.write("Enter two words to check if they are anagrams")

word1 = st.text_input("Enter the first word:")
word2 = st.text_input("Enter the second word:")

if st.button("Check Anagram"):
    if check_anagram(word1, word2):
        st.write(f"'{word1}' and '{word2}' are anagrams!")
    else:
        st.write(f"'{word1}' and '{word2}' are not anagrams.")