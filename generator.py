import streamlit as st
import requests

# Function to call the API and get the text summary
def api_function(instructions):
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    api_response = requests.post('https://text-summarization.agreeabledune-08a9cefb.switzerlandnorth.azurecontainerapps.io/api/v1/classify', json={"text": instructions}, headers=headers)
    if api_response.status_code == 200:
        return api_response.json()[0]["answer"]

# Streamlit app UI
st.title("Text Summarization App")

text_input = st.text_area("Enter the text you want to summarize:")
if st.button("Summarize"):
    if text_input:
        summary = api_function(text_input)
        st.header("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")