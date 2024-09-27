import streamlit as st
import re

def main():
    st.title("Letter Counter")
    
    sentence = st.text_input("Enter a sentence:")

    if not sentence:
        st.error("Please enter a sentence.")
    else:
        letters = re.sub(r'\W+', '', sentence).lower()
        letter_count = len(letters)
        
        st.header(f"The sentence '{sentence}' contains {letter_count} letters.")

if __name__ == "__main__":
    main()