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
        entity_list = api_response["response"].strip('[]').split(', ')
        count = 1
        
        for entity in entity_list:
            results_str += str(count) + ". " + entity + "\n"
            count += 1
        return results_str

st.title("Named Entity Recognition App")

text_input = st.text_area("Enter your text:")
if st.button("Name Entities"):
    if text_input:
        named_entities = api_function(text_input)
        st.write("Named Entities:")
        st.write(named_entities)
    else:
        st.write("Please enter some text.")