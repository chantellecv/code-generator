import streamlit as st
from collections import Counter

# Function to check if a word is an anagram
def is_anagram(word, word_list):
    word = word.lower()
    word_characters = [char for char in word if char.isalpha()]
    word_count = Counter(word_characters)

    for anagram_word in word_list:
        anagram_word = anagram_word.lower()
        anagram_word_characters = [char for char in anagram_word if char.isalpha()]
        anagram_word_count = Counter(anagram_word_characters)

        if word_count == anagram_word_count:
            return True

    return False

# Predefined list of words
anagram_words = ["listen", "silent", "enlist", "inlet", "tinsel", "tennis", "taste", "tents", "tenet", "site", "tie", "sit", "sin", "net", "noe", "ten", "sent", "tie", "ten"]

# Streamlit app
if __name__ == "__main__":
    st.title("Anagram Checker")

    word_input = st.text_input("Enter a word to check for anagrams:")

    if st.button("Check"):
        if not word_input:
            st.write("Please enter a word to check.")
        else:
            result = is_anagram(word_input, anagram_words)
            if result:
                st.write(f"'{word_input}' is an anagram of one of the predefined words.")
            else:
                st.write(f"'{word_input}' is not an anagram of any of the predefined words.")