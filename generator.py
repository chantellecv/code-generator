import streamlit as st

def main():
    st.title('Word Checker App')
    
    word1 = st.text_input("Enter the first word:")
    word2 = st.text_input("Enter the second word:")
    
    if word1 == word2:
        st.write("The words are the same!")
    else:
        st.write("The words are different!")

if __name__ == '__main__':
    main()