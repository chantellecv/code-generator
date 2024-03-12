import streamlit as st

# Placeholder for the function to interact with the model
def generate_essay(topic, word_count=500):
    """
    Function to generate an essay based on a given topic.
    This should be replaced with actual calls to a text generation model or API.
    """
    # Assume this returns a 500-word essay on the specified topic
    generated_text = f"This is a generated essay on the topic '{topic}' with approximately {word_count} words."
    return generated_text

# Streamlit app interface
st.title("500-Word Essay Generator")

# User input for the essay topic
topic = st.text_input("Enter the essay topic:", "")

# Button to trigger essay generation
if st.button("Generate Essay"):
    if topic:
        # Generating essay
        essay = generate_essay(topic)
        
        # Displaying the generated essay
        st.write(essay)
    else:
        st.error("Please enter a topic to generate an essay.")

if __name__ == "__main__":
    st.mainloop()