import streamlit as st
import openai

# Initialize OpenAI client with your API key
openai.api_key = 'your_api_key_here'

def generate_essay(prompt, word_count=500):
    response = openai.Completion.create(
        engine="text-davinci-003",  # As of my last update, text-davinci-003 is a powerful model. Update if needed
        prompt=prompt,
        max_tokens=word_count*0.8,  # Roughly estimate the tokens to match a 500-word essay. May need adjustment.
        temperature=0.7,  # Adjusts randomness. Closer to 1 makes it more diverse; closer to 0 more deterministic.
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n\n"]  # Optional: Defines stop sequence. Adjust based on your needs.
    )
    return response.choices[0].text.strip()

def main():
    st.title("500-Word Essay Generator")

    # User input for essay topic
    topic = st.text_input("Enter the essay topic:", "")

    if st.button("Generate Essay"):
        if topic.strip() != "":
            with st.spinner('Generating...'):
                essay = generate_essay(topic)
                st.subheader("Generated Essay:")
                st.write(essay)
        else:
            st.error("Please enter a valid topic.")

if __name__ == "__main__":
    main()