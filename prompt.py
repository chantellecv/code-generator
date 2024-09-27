from dotenv import load_dotenv
import os
import streamlit as st
from openai import OpenAI
from groq import Groq
from github import Github


load_dotenv()

summary = '''def api_function(instructions):
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    api_response = requests.post('https://text-summarization.agreeabledune-08a9cefb.switzerlandnorth.azurecontainerapps.io/api/v1/classify', json={"text": instructions}, headers=headers)
    if api_response.status_code == 200:
        return api_response.json()[0]["answer"]'''


NER = '''def api_function(instructions):
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    api_response = requests.post('https://text-named-er-spacy.icysmoke-f4846de1.switzerlandnorth.azurecontainerapps.io/api/v1/entity-recognition', json={"text": instructions}, headers=headers)
    
    if api_response.status_code == 200:
        results_str = " "
        entity_list = api_response.json()["response"].strip('[]\'').split('\', \'') 
        count = 1
    
        for entity in entity_list:
            results_str += str(count) + ". " + entity + "\n"
            count += 1
        return results_str '''

def generate_code(prompt, chat_log):
    # client = OpenAI(
    #     # ENTER YOUR OPENAI API KEY
    #     api_key=os.getenv("GROQ_KEY"),
    #     base_url="https://api.groq.com/openai/v1",
    # )
    client = Groq(
        api_key=os.getenv("GROQ_KEY"),
    )

    response = client.chat.completions.create(
        # model="gpt-4-turbo-preview",
        # model="gpt-3.5-turbo",
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are an assistant that generates Python code for a Streamlit app based on a user's prompt and an api functions provided. The generated code will be deployed to the Streamlit app where the user will be able to interact with their app."},
            # {"role": "assistant", "content": summary},
            # {"role": "assistant", "content": NER},
            {"role": "assistant", "content": chat_log},
            {"role": "user", "content": prompt}   
        ]
    )
    chat_log += f'\nUser: {prompt}\nAssistant: {response.choices[0].message.content}\n'
    # st.write(chat_log)
    # st.write("end of log")
    code = response.choices[0].message.content
    python_code = extract_python_code(code)
    return python_code, chat_log


def extract_python_code(output_text):
    start_index = output_text.find("```") + len("```")
    end_index = output_text.find("```", start_index)
    
    if start_index != -1 and end_index != -1:
        python_code = output_text[start_index:end_index]
    else:
        python_code = "" 
    # st.text(python_code)
    
    return python_code.strip()


def push_to_github(repo_name, file_name, content, token):
    try:
        g = Github(token)
        user = g.get_user()
        try:
            repo = user.get_repo(repo_name)
            try:
                old_file = repo.get_contents(file_name)
                # Update the existing file
                repo.update_file(file_name, "Update file", content, old_file.sha)
                return True, None
            except:
                # File doesn't exist, create a new one
                repo.create_file(file_name, "Initial commit", content)
                return True, None
        except:           
            # Repository doesn't exist, create a new one
            repo = user.create_repo(repo_name)
            repo.create_file(file_name, "Initial commit", content)
            return True, None
    except Exception as e:
        return False, str(e)
    


    
def clicked(button):
    st.session_state.clicked[button] = True
    
def main():
    
    if 'clicked' not in st.session_state:
        st.session_state.clicked = {1:False, 2:False, 3:False}
    
    st.title("App Builder")

    yes = st.checkbox("Show code")
    
    # Input prompt from user
    prompt = st.text_area("What would you like to build?", placeholder = "I want to build...")
    generated_code = ""
    
    if 'chat_log' not in st.session_state:
        st.session_state.chat_log = ""
    
    if yes:
        
        st.button("Generate Code for Review", on_click=clicked, args=[1])
        
        if st.session_state.clicked[1]:
                    
            with st.spinner("Generating Code..."): 

                st.divider()
                generated_code, st.session_state.chat_log = generate_code(prompt, st.session_state.chat_log)

                if generated_code != "":
                
                    repo_name = 'code-generator'
                    file_name = 'generator.py'
                    
                    # ENTER YOUR GITHUB TOKEN
                    github_token = os.getenv("GITHUB_API_KEY")

                    modified_code = st.text_area("**Generated code**", value=generated_code, height=400)
                    
                    # st.write(st.session_state.clicked[3])
                    st.button("Build App", on_click=clicked, args=[3])
                    
                    # if st.session_state.clicked[3]:
                        
                    with st.spinner("Building App..."): 
            
                        success, message = push_to_github(repo_name, file_name, modified_code, github_token)
                        # st.write('pushed')
                        if success:
                            st.success("App built successfully!")
                            st.write('''Click [here](https://code--generator.streamlit.app) to view your app.                     
                            Alternatively, copy and paste the following link in your browser: https://code--generator.streamlit.app''')
                    
                        else:
                            st.error(f"Failed to build app: {message}")
                
        st.session_state.clicked[1] = False
        
    else:
        
        st.button("Build App", on_click=clicked, args=[2], key='automatic')

        if  st.session_state.clicked[2]:
        
            with st.spinner("Building App..."): 

                st.divider()
                generated_code, st.session_state.chat_log = generate_code(prompt, st.session_state.chat_log)
                # st.write("generated code is: ", generated_code)
                if generated_code != "":
                
                    repo_name = 'code-generator'
                    file_name = 'generator.py'
                    
                    # ENTER YOUR GITHUB TOKEN
                    github_token = os.getenv("GITHUB_API_KEY")
  
                    success, message = push_to_github(repo_name, file_name, generated_code, github_token)
                    # st.write('pushed')
                    if success:
                        st.success("App built successfully!")
                        st.write('''Click [here](https://code--generator.streamlit.app) to view your app.                     
                        Alternatively, copy and paste the following link in your browser: https://code--generator.streamlit.app''')
                
                    else:
                        st.error(f"Failed to build app: {message}")
                
        st.session_state.clicked[2] = False
            
        
        
        
        
        
        # st.write(3) 
        # st.write(st.session_state.clicked)
                    
            # yes = st.checkbox("Show code")
            # if yes == True:
            #     st.code(generated_code, language='python')

    
    # if yes and generated_code:
    #         # Display the generated code
    #     # st.text_area("Generated Code", value=generated_code, height=400)

    #     # Textarea for users to modify the code
    #     modified_code = st.text_area("*Generated Code*\nModify Code (Optional)", value=generated_code, height=400)

    #     # Button to push the modified code to GitHub repo
    #     if st.button("Push Modified Code"):
    #         with st.spinner("Pushing Modified Code..."):
    #             # If modified code is provided, push it to GitHub
    #             if modified_code:
    #                 success, message = push_to_github(repo_name, file_name, modified_code, github_token)
    #                 if success:
    #                     st.success("Modified code pushed successfully to GitHub!")
    #                 else:
    #                     st.error(f"Failed to push modified code: {message}")
    #             else:
    #                 st.warning("No modified code provided.")
            


if __name__ == "__main__":
    main()