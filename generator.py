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

st.title("Text Summarization App")

text1 = st.text_area("Enter Text 1:")
text2 = st.text_area("Enter Text 2:")

if st.button("Summarize"):
    if text1 and text2:
        summary1 = api_function(text1)
        summary2 = api_function(text2)
        
        st.write("Summary of Text 1:")
        st.write(summary1)
        
        st.write("Summary of Text 2:")
        st.write(summary2)