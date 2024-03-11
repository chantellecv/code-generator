import streamlit as st
from chatgpt import ChatGPT

# Initialize the ChatGPT model with GPT-3
chatbot = ChatGPT(engine="gpt3")

# Streamlit app title and description
st.title("Chatbot Application")
st.write("Welcome to the conversational chatbot. Start typing to chat with the chatbot!")

# User input text box
user_input = st.text_input("You:", "")

# Chatbot response
if st.button("Send"):
    if user_input:
        # Generate a response from the chatbot
        response = chatbot.get_response(user_input)
        st.text_area("Chatbot:", value=response)