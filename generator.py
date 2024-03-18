import streamlit as st
import requests

def api_function(instructions):
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    api_response = requests.post('https://text-summarization.agreeabledune-08a9cefb.switzerlandnorth.azurecontainerapps.io/api/v1/classify', json={"text": instructions}, headers=headers)
    if api_response.status_code == 200:
        return api_response.json()[0]["answer"]

# Streamlit app
st.title("Text Summarizer App")
text = st.text_area("Enter the text you want to summarize:")
if st.button("Summarize"):
    if text:
        summary = api_function(text)
        st.write("Summary:")
        st.write(summary)
    else:
        st.write("Please enter some text to summarize.")