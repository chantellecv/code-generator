import streamlit as st
import pandas as pd

# Load ticket data from backend data storage
ticket_data = pd.read_csv('ticket_data.csv')

# Display total number of tickets
total_tickets = ticket_data.shape[0]
st.write(f'Total Number of Tickets: {total_tickets}')

# Display tickets by category
ticket_category = st.selectbox('Select Category', ticket_data['Category'].unique())
category_tickets = ticket_data[ticket_data['Category'] == ticket_category]
st.write(f'Tickets in Category "{ticket_category}": {category_tickets.shape[0]}')

# Display ticket status
ticket_status = st.selectbox('Select Status', ['Open', 'Closed', 'Pending'])
status_tickets = ticket_data[ticket_data['Status'] == ticket_status]
st.write(f'Tickets with Status "{ticket_status}": {status_tickets.shape[0]}')

# Backend to handle data storage and real-time updates
# This code will be deployed to the backend server provided by Streamlit

# Define a function to update the ticket data
@st.cache
def update_ticket_data():
    global ticket_data
    ticket_data = pd.read_csv('updated_ticket_data.csv')

# Real-time update button
if st.button('Update Ticket Data'):
    update_ticket_data()
    st.write('Ticket data updated successfully')