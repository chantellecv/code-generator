import streamlit as st
import requests

def api_function(instructions):
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    api_response = requests.post('https://text-named-er-spacy.icysmoke-f4846de1.switzerlandnorth.azurecontainerapps.io/api/v1/entity-recognition', json={"text": instructions}, headers=headers)
    
    if api_response.status_code == 200:
        results_str = " "
        entity_list = api_response.json()["response"].strip('[]').split(', ')
        count = 1
    
        for entity in entity_list:
            results_str += str(count) + ". " + entity + "\n"
            count += 1
        return results_str

st.title("Entity Recognition App")
text = st.text_area("Enter your text here:")

if st.button("Identify Entities"):
    if text:
        entities = api_function(text)
        st.write("Entities identified in the text:")
        st.write(entities)
    else:
        st.warning("Please enter some text to identify entities.")