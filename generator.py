import streamlit as st
import requests

# Title of the app
st.title('Text Summarizer')

# Input field for user to enter the text to be summarized
text = st.text_area('Enter the text to be summarized:', height=200)

# Button to summarize the text
if st.button('Summarize Text'):
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    api_response = requests.post('https://text-summarization.agreeabledune-08a9cefb.switzerlandnorth.azurecontainerapps.io/api/v1/classify', json={"text": text}, headers=headers)

    if api_response.status_code == 200:
        summary = api_response.json()[0]["answer"]
        st.success('Summary:')
        st.write(summary)