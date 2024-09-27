import streamlit as st

# Create a Streamlit app
st.title("Word Counter")

# Create a text input for the user to enter a sentence
sentence_input = st.text_input("Enter a sentence:")

# Create a button to trigger the word counting
if st.button("Count words"):
    # Get the sentence from the input
    sentence = sentence_input.strip()
    
    # Count the number of words
    word_count = len(sentence.split())
    
    # Display the result
    st.write(f"The sentence contains thisss manyyyy {word_count} words.")