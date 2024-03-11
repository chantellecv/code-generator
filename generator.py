import streamlit as st

# Set up menu items with prices
menu = {
    'Burger': 5.99,
    'Pizza': 8.99,
    'Fries': 2.49,
    'Drink': 1.99
}

st.title('Self-Ordering Kiosk App')

# Display menu items
st.header('Menu')
order = {}
for item, price in menu.items():
    qty = st.number_input(f'{item} - ${price}', min_value=0, step=1)
    if qty > 0:
        order[item] = qty

# Calculate total order amount
total_amount = sum([menu[item] * qty for item, qty in order.items()])

# Display order summary
st.header('Order Summary')
for item, qty in order.items():
    st.write(f'{item}: {qty}')

st.write(f'Total amount: ${total_amount}')