import streamlit as st
from collections import Counter
import enchant
import itertools

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

# Function to generate all possible combinations of characters in a word
def generate_anagrams(word):
    word = word.lower()
    word_characters = [char for char in word if char.isalpha()]
    anagrams = [''.join(p) for p in itertools.permutations(word_characters)]
    return anagrams

# Function to check if a word is valid
def is_valid(word):
    d = enchant.Dict("en_US")
    return d.check(word)

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
            anagrams = generate_anagrams(word_input)
            valid_anagrams = [anagram for anagram in anagrams if is_valid(anagram) and is_anagram(anagram, anagram_words)]
            if valid_anagrams:
                st.write(f"'{word_input}' is an anagram of the following words: {', '.join(valid_anagrams)}")
            else:
                st.write(f"'{word_input}' is not an anagram of any of the predefined words. Here are possible anagrams: {', '.join([anagram for anagram in anagrams if is_valid(anagram)])}")