import streamlit as st
import random

# Function to get a random French vocabulary question
def get_vocabulary_question():
    question_set = [
        {"question": "What is the French word for 'Apple'?", "options": ['Pomme', 'Banane', 'Orange'], "answer": "Pomme"},
        {"question": "What is the French word for 'Book'?", "options": ['Livre', 'Stylo', 'Table'], "answer": "Livre"},
        {"question": "What is the French word for 'Car'?", "options": ['Chaise', 'Voiture', 'Fenêtre'], "answer": "Voiture"},
    ]
    return random.choice(question_set)

# Basic layout and title of the app
st.title('Learn French with Fun!')

# User's name input
name = st.text_input('What is your name?')

if name:
    # Welcome message
    st.write(f"Bonjour {name}! Ready to learn French? Let's start!")

    # Selecting the type of exercise
    exercise = st.selectbox('Choose an exercise type:', ['Choose', 'Vocabulary', 'Grammar', 'Games'])

    if exercise == 'Vocabulary':
        st.subheader('Vocabulary Exercise')
        question = get_vocabulary_question()
        answer = st.radio(question['question'], question['options'])

        if st.button('Submit'):
            if answer == question['answer']:
                st.success('Correct! 🎉')
            else:
                st.error('Oops! The correct answer is: ' + question['answer'])

    elif exercise == 'Grammar':
        st.subheader('Grammar exercises coming soon!')
        st.write("We're working on adding more content. Stay tuned!")

    elif exercise == 'Games':
        st.subheader('Language games coming soon!')
        st.write("Fun games are on the way. Check back later!")

# Footer
st.markdown('---')
st.write('Merci for using our app to learn French!')