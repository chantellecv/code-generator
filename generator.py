# Import necessary libraries
import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot('MyChatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English language
trainer.train("chatterbot.corpus.english")

# Function to get response from the chatbot
def get_response(message):
    return chatbot.get_response(message)

# Streamlit App
st.title('Python Chatbot')

# User input textbox
user_input = st.text_input('You:')

# Bot response
if st.button('Send'):
    bot_response = get_response(user_input)
    st.write('Bot:', bot_response)