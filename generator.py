import streamlit as st
import re

# Function to check if a word is a palindrome
def is_palindrome(word):
    word = re.sub(r'\W+', '', word).lower()
    return word == word[::-1]

# Function to get all substrings of a word
def get_substrings(word):
    substrings = []
    for i in range(len(word)):
        for j in range(i+1, len(word)+1):
            substrings.append(word[i:j])
    return substrings

# Function to filter even length substrings
def get_even_substrings(word):
    substrings = get_substrings(word)
    even_substrings = [s for s in substrings if len(s) % 2 == 0]
    return even_substrings

# Streamlit app
if __name__ == "__main__":
    st.title("Palindrome and Even Substring Finder")

    word_input = st.text_input("Enter a word to check:")

    if st.button("Check"):
        if not word_input:
            st.write("Please enter a word.")
        else:
            if is_palindrome(word_input):
                st.write(f"{word_input} is a palindrome!")
                st.write("Here are its even substrings:")
                for substring in get_even_substrings(word_input):
                    st.write(substring)
            else:
                st.write(f"{word_input} is not a palindrome.")