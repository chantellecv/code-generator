Python
import streamlit as st
from st_aggrid import AgGrid

st.title("Word Counter")

# Load the AG Grid library
grid_options = {"columnDefs": [{"field": "word", "headerName": "Word"}]}
ag_grid = AgGrid(st.empty(), gridOptions=grid_options)

paragraph = st.text_area("Please enter the paragraph to count the number of words:")

if st.button("Count"):
    try:
        words = paragraph.split()
        result = len(words)
        st.success(f"There are {result} words in the paragraph.")
        ag_grid.update_data([[word] for word in words])
    except:
        st.error("Invalid input")