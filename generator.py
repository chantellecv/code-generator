import streamlit as st
import re

def main():
    st.title("Word Counter")
    
    sentence = st.text_input("Enter a sentence:")

    if not sentence:
        st.error("Please enter a sentence.")
    else:
        words = re.split(r'\W+', sentence)
        word_count = len(words)
        
        st.header(f"The sentence '{sentence}' contains {word_count} words.")

if __name__ == "__main__":
    main()