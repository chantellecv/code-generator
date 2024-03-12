import streamlit as st
import random

# Simulated question bank for a simple Spanish vocabulary quiz
question_bank = {
    "apple": "manzana",
    "house": "casa",
    "book": "libro",
    "tree": "árbol",
    "car": "coche",
}

def generate_question():
    """Randomly selects a question from the question bank."""
    question, answer = random.choice(list(question_bank.items()))
    return question, answer

def check_answer(question, user_answer):
    """Checks if the user's answer is correct."""
    correct_answer = question_bank[question]
    return user_answer.lower().strip() == correct_answer.lower().strip()

# Streamlit App Layout
st.title("Language Learning App")

# Selecting the game mode
game_mode = st.radio("Choose your learning mode:", ("Vocabulary Quiz", "About"))

if game_mode == "Vocabulary Quiz":
    st.header("Vocabulary Quiz: English to Spanish")

    if 'question' not in st.session_state or st.button("Get New Word"):
        st.session_state.question, _ = generate_question()

    question = st.session_state.question
    st.write(f"What is the Spanish word for: **{question}**?")
    
    user_answer = st.text_input("Your answer:")

    if st.button("Check Answer"):
        if check_answer(question, user_answer):
            st.success("Correct! Great job!")
        else:
            st.error(f"Oops! The correct answer is **{question_bank[question]}**.")
            
elif game_mode == "About":
    st.write("""
        This app is designed to help users learn new languages through interactive exercises, quizzes, and games. 
        Currently, it features a simple vocabulary quiz to translate words from English to Spanish. 
        Future updates will include more languages, comprehensive exercises, and engaging language games. Stay tuned!
    """)