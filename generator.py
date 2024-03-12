import streamlit as st
import random

# Set the title of the app
st.title("Language Learning App")

# Define a list of languages for the user to choose from
languages = ["Spanish", "French", "German", "Italian"]

# Create a selectbox for the user to choose the language
selected_language = st.selectbox("Select a language to learn", languages)

# Language-specific interactive exercises, quizzes, and games
if selected_language == "Spanish":
    st.write("Hola! Welcome to the Spanish Language Learning Section")
    # Add interactive exercises, quizzes, and games for learning Spanish here
elif selected_language == "French":
    st.write("Bonjour! Welcome to the French Language Learning Section")
    # Add interactive exercises, quizzes, and games for learning French here
elif selected_language == "German":
    st.write("Hallo! Welcome to the German Language Learning Section")
    # Add interactive exercises, quizzes, and games for learning German here
elif selected_language == "Italian":
    st.write("Ciao! Welcome to the Italian Language Learning Section")
    # Add interactive exercises, quizzes, and games for learning Italian here