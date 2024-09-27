import streamlit as st

# Create a title for the app
st.title("Word Counter")

# Create a text area for the user to enter the first sentence
sentence1_input = st.text_input("Please enter the first sentence:")

# Create a text area for the user to enter the second sentence
sentence2_input = st.text_input("Please enter the second sentence:")

# Create a button to trigger the counting process
if st.button("Count"):
    # Split the sentences into words and count them
    words1 = sentence1_input.split()
    words2 = sentence2_input.split()
    word_count1 = len(words1)
    word_count2 = len(words2)
    
    # Display the results
    st.success(f"The first sentence has {word_count1} words.")
    st.success(f"The second sentence has {word_count2} words.")