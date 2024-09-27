import streamlit as st

# Create a title for the app
st.title("Word Counter")

# Create a text area for the user to enter the sentence
sentence_input = st.text_input("Please enter your sentence:")

# Create a button to trigger the counting process
if st.button("Count"):
    # Split the sentence into words and count them
    words = sentence_input.split()
    word_count = len(words)
    
    # Display the results
    st.success(f"The sentence has {word_count} words.")