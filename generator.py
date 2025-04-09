import streamlit as st

# Authentication
username = st.text_input("Username")
password = st.text_input("Password", type="password")
if st.button("Login"):
    # Add authentication logic here
    st.success("Login successful!")

# Update ticket status
selected_ticket = st.selectbox("Select a ticket to update status", ["Ticket 1", "Ticket 2", "Ticket 3"])
new_status = st.selectbox("Select new status", ["Active", "Resolved", "Pending"])
if st.button("Update Status"):
    # Add ticket status update logic here
    st.success(f"Ticket status updated for {selected_ticket} to {new_status}")

# Add new ticket
new_ticket = st.text_input("Enter new ticket details")
assigned_user = st.text_input("Assign to user")
if st.button("Add Ticket"):
    # Add new ticket logic here
    st.success(f"New ticket added: {new_ticket}. Assigned to {assigned_user}")

# Display tickets
st.subheader("Tickets Overview")
active_tickets = 10
resolved_tickets = 5
pending_tickets = 3

st.write(f"Active Tickets: {active_tickets}")
st.write(f"Resolved Tickets: {resolved_tickets}")
st.write(f"Pending Tickets: {pending_tickets}")