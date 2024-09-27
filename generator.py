import streamlit as st

def main():
    st.title("Word Counter")
    
    sentence = st.text_input("Enter a sentence:")

    if not sentence:
        st.error("Please enter a sentence.")
    else:
        words = sentence.split()
        word_count = len(words)
        
        st.header(f"The sentence '{sentence}' contains {word_count} words.")

if __name__ == "__main__":
    main()