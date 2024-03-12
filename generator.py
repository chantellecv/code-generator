import streamlit as st

# Function to display the home page
def home_page():
    st.header("Welcome to the French Learning App!")
    st.write("Select an activity from the left sidebar to start learning.")

# Function for a basic vocabulary exercise
def vocabulary_practice():
    st.header("Vocabulary Practice")
    st.write("Translate the following English words into French.")

    vocab_questions = {
        "apple": "pomme",
        "book": "livre",
        "car": "voiture"
        # Add more vocab here
    }
    score = 0

    for word, correct_answer in vocab_questions.items():
        user_answer = st.text_input(f"What is the French word for '{word}'?", "").lower()
        if user_answer == correct_answer:
            st.success("Correct!")
            score += 1
        elif user_answer != "":
            st.error(f"Oops! The correct answer is '{correct_answer}'.")

    st.write(f"Your score: {score}/{len(vocab_questions)}")

# Function for a basic grammar quiz
def grammar_quiz():
    st.header("Grammar Quiz")
    st.write("Choose the correct option.")

    quiz_questions = [
        {"question": "How do you say 'I am' in French?", "options": ["Je suis", "Tu es", "Il est"], "answer": "Je suis"},
        # Add more quiz questions here
    ]
    score = 0

    for quiz in quiz_questions:
        user_answer = st.radio(quiz["question"], quiz["options"], key=quiz["question"])
        if user_answer == quiz["answer"]:
            st.success("That's right!")
            score += 1
        else:
            st.error("Try again!")

    st.write(f"Your score: {score}/{len(quiz_questions)}")

# Sidebar navigation
st.sidebar.title("Navigation")
app_mode = st.sidebar.radio("Go to", ["Home", "Vocabulary Practice", "Grammar Quiz"])

if app_mode == "Home":
    home_page()
elif app_mode == "Vocabulary Practice":
    vocabulary_practice()
elif app_mode == "Grammar Quiz":
    grammar_quiz()