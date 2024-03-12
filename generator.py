import streamlit as st
import openai

# Replace "your_api_key_here" with your actual OpenAI API key
openai.api_key = 'your_api_key_here'

# Streamlit app title
st.title('500-Word Essay Generator')

# Input for the essay topic
topic = st.text_input('Enter the essay topic:', '')

# Function to generate essay
def generate_essay(topic):
    try:
        # Adjust parameters as necessary
        response = openai.Completion.create(
          engine="text-davinci-003",  # You can choose a different model here
          prompt=f"Write a 500-word essay about {topic}.",
          temperature=0.7,
          max_tokens=4000,  # Adjust based on the model's limits and desired output length
          top_p=1.0,
          frequency_penalty=0.0,
          presence_penalty=0.0
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Button to generate essay
if st.button('Generate Essay'):
    if topic:
        with st.spinner('Generating essay...'):
            essay = generate_essay(topic)
            st.text_area('Generated Essay:', essay, height=250)
    else:
        st.error('Please enter a topic to generate the essay.')