import streamlit as st
import random

def generate_story(theme, character):
    """
    Generates a short story based on the specified theme and character.
    This is a simple implementation and can be expanded with more complex logic or AI models.
    """
    beginnings = [
        f"One day, {character} woke up to find out that everything had changed overnight.",
        f"In a world where {theme} dominated, {character} found themselves at a crossroads.",
        f"Never had {character} imagined they would be part of a {theme}, yet here they were."
    ]

    middles = [
        "It wasn't long before things started to get interesting.",
        "As the journey continued, challenges and allies appeared in the most unexpected places.",
        "With a heavy heart and a clear mind, the quest for a solution had truly begun."
    ]

    ends = [
        f"In the end, it all boiled down to what {character} truly believed in.",
        "And so, with a final push, a new chapter began, ripe with possibilities.",
        "The adventure may have concluded, but the memories and lessons lingered on."
    ]

    # Randomly select parts of the story
    beginning = random.choice(beginnings)
    middle = random.choice(middles)
    end = random.choice(ends)

    # Combine and return the story
    story = f"{beginning} {middle} {end}"
    return story

def main():
    st.title("Creative Short Story Generator")

    # User inputs
    theme = st.text_input("Enter a theme for the story (e.g., adventure, mystery):")
    character = st.text_input("Enter the main character's name:")

    # Story generation button
    generate = st.button("Generate Story")

    if generate and theme and character:
        # Generate and display the story
        story = generate_story(theme, character)
        st.subheader("Here's your story:")
        st.write(story)
    elif generate:
        st.error("Please enter both a theme and a character's name to generate a story.")

if __name__ == "__main__":
    main()