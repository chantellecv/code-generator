import streamlit as st
import random

# Dictionary of language exercises with questions and answers
exercises = {
    "Translate the word 'hello' in the new language": "Bonjour",
    "Translate the word 'goodbye' in the new language": "Au revoir",
    "Translate the word 'thank you' in the new language": "Merci",
    "Translate the word 'yes' in the new language": "Oui",
    "Translate the word 'no' in the new language": "Non",
}

# Language games
def language_quiz(exercises):
    score = 0
    for question, answer in exercises.items():
        user_answer = st.text_input(question)
        if user_answer.lower() == answer.lower():
            st.write("Correct!")
            score += 1
        else:
            st.write(f"Incorrect. The correct answer is: {answer}")
    st.write(f"Your final score is: {score}/{len(exercises)}")

# Main section of the app
st.title("Language Learning App")

option = st.sidebar.selectbox(
    "Choose an option:",
    ["Language Exercises", "Language Quiz"]
)

if option == "Language Exercises":
    st.subheader("Language Exercises")
    exercise = random.choice(list(exercises.keys()))
    st.write(exercise)

elif option == "Language Quiz":
    st.subheader("Language Quiz")
    language_quiz(exercises)