import streamlit as st
import requests

def api_function(instructions):
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    api_response = requests.post('https://text-summarization.agreeabledune-08a9cefb.switzerlandnorth.azurecontainerapps.io/api/v1/classify', json={"text": instructions}, headers=headers)
    
    if api_response.status_code == 200:
        summarised_text = api_response.json()[0]["answer"]
        
        api_response_entities = requests.post('https://text-named-er-spacy.icysmoke-f4846de1.switzerlandnorth.azurecontainerapps.io/api/v1/entity-recognition', json={"text": summarised_text}, headers=headers)
    
        if api_response_entities.status_code == 200:
            results_str = " "
            entity_list = api_response_entities.json()["response"].strip('[]'').split('', '')
            count = 1
        
            for entity in entity_list:
                results_str += str(count) + ". " + entity + "
"
                count += 1
            return summarised_text, results_str
        else:
            return "Error in identifying entities."
    else:
        return "Error in summarizing text."

st.title("Text Summarization and Entity Recognition App")

user_input = st.text_area("Enter text to summarize and identify entities:")

if st.button("Summarize and Identify Entities"):
    with st.spinner("Summarizing and identifying entities..."):
        summary, entities = api_function(user_input)
        st.subheader("Summarized Text:")
        st.write(summary)
        st.subheader("Identified Entities:")
        st.write(entities)