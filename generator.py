import streamlit as st

# Dictionary of available items and their prices
menu = {
    'Burger': 5.99,
    'Fries': 2.49,
    'Salad': 4.99,
    'Drink': 1.99
}

st.title('Self-Ordering Kiosk App')

# Display the menu
st.write('### Menu:')
for item, price in menu.items():
    st.write(f'- {item}: ${price}')

# Initialize order
order = {}

# Allow users to select items and quantities
st.write('### Select Items:')
for item in menu.keys():
    quantity = st.number_input(f'Quantity of {item}', min_value=0, step=1)
    if quantity > 0:
        order[item] = quantity

# Calculate and display total cost
total_cost = sum([menu[item] * quantity for item, quantity in order.items()])
st.write('### Total Cost:')
st.write(f'${total_cost:.2f}')

# Display order summary
if order:
    st.write('### Order Summary:')
    for item, quantity in order.items():
        st.write(f'- {item}: {quantity}')