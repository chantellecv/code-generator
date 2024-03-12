import streamlit as st
import random

# Function to generate the story
def generate_story(theme, character):
    # Basic story elements
    beginnings = {
        'adventure': f"One day, {character} found a mysterious map leading to an unknown land.",
        'horror': f"It was a dark, stormy night when {character} heard a strange noise coming from the basement.",
        'fantasy': f"In the realm of Eldoria, {character} stumbled upon an ancient artifact of immense power.",
    }
    
    middles = {
        'adventure': f"Braving through treacherous paths, {character} encountered various challenges.",
        'horror': f"Every corner of the house seemed to hide dark secrets, terrifying {character} more with each step.",
        'fantasy': f"With the artifact, {character} set out on a quest to defeat the dark sorcerer threatening the land.",
    }
    
    ends = {
        'adventure': f"Finally, after many hardships, {character} discovered the treasure, bringing prosperity to their village.",
        'horror': f"In the end, {character} uncovered the truth behind the haunting, bringing peace to the restless spirits.",
        'fantasy': f"The battle was fierce, but {character} emerged victorious, hailed as a hero throughout Eldoria.",
    }

    # Generating the story by concatenating parts
    story = f"{beginnings.get(theme, 'Once upon a time,')}\n\n{middles.get(theme, '')}\n\n{ends.get(theme, 'And they lived happily ever after.')}"
    return story

# Streamlit UI
def main():
    st.title("Creative Short Story Generator")
    
    # User inputs
    theme = st.selectbox("Select the theme of your story:", ('adventure', 'horror', 'fantasy'), index=0)
    character = st.text_input("Enter the name of your main character:", "Alex")

    # Button to generate story
    if st.button("Generate Story"):
        story = generate_story(theme, character)
        st.subheader("Here's your story:")
        st.write(story)

if __name__ == "__main__":
    main()