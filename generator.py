import streamlit as st
import re

# Define a function to count the occurrences of a text in a string
def count_occurrences(string, text):
    # Use regular expression to find the occurrences of the text
    occurrences = re.findall(text.lower(), string.lower())
    return len(occurrences)

# Create a Streamlit app
st.title("Text Counter")
st.header("Enter a string and a text to search: ")

# Create text input fields for user input
string_input = st.text_area("String", value='')
text_input = st.text_input("Search Text", value='')

# If the user has input a string and a search text, count the occurrences
if string_input and text_input:
    try:
        string = string_input.strip()
        text = text_input.strip()
        occurrences = count_occurrences(string, text)
        st.write(f"The text '{text}' occurs {occurrences} times in the string.")
    except Exception as e:
        st.error(f"Error: {str(e)}")
else:
    st.write("Please enter a string and a text to search!")