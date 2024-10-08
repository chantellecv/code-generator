import streamlit as st
import pandas as pd

# Data
data = {
    "Category": ["IT", "HR", "Marketing", "Sales", "IT", "HR", "Marketing", "Sales"],
    "Department": ["Software Development", "Recruitment", "Digital Marketing", "Business Development", "Networking", "Employee Relations", "Content Creation", "Sales Support"],
    "Priority": [1, 2, 3, 4, 5, 6, 7, 8]
}

df = pd.DataFrame(data)

# Function to find the best department
def find_best_department(df, category):
    best_department = df.loc[(df["Category"] == category)].sort_values(by='Priority').head(1)
    return best_department["Department"].values[0]

# Create Streamlit App
st.title("Department Finder")

# Get user input
category = st.selectbox("Select a category", sorted(df["Category"].unique()), key=("SELECT_CATEGORY"))

# Check if the input is valid
if category:
    best_department = find_best_department(df, category)
    st.write(f"The best department for {category} is {best_department}")
else:
    st.write("Please select a category.")