Python
import streamlit as st
import re

def main():
    st.title("Word Counter")
    
    paragraph = st.text_area("Enter a paragraph:")
    
    if not paragraph:
        st.error("Please enter a paragraph.")
    else:
        words = re.split(r'\W+', paragraph)
        word_count = len([word for word in words if word != ''])
        
        st.header(f"The paragraph contains {word_count} words.")

if __name__ == "__main__":
    main()