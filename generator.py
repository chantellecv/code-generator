import streamlit as st

# Menu items with prices
menu = {
    'Burger': 5.99,
    'Pizza': 8.99,
    'Salad': 4.99,
    'Drink': 1.99
}

st.title('Self-Ordering Kiosk')

# Display menu
st.write('Menu:')
for item, price in menu.items():
    st.write(f'{item}: ${price}')

# Initialize order
order = {}

# Select items to order
st.write('\nSelect items to order:')
for item in menu:
    quantity = st.number_input(f'How many {item}s?', min_value=0, max_value=10)
    if quantity > 0:
        order[item] = quantity

# Display order summary
st.write('\nOrder Summary:')
total_cost = 0
for item, quantity in order.items():
    cost = menu[item] * quantity
    st.write(f'{item}: {quantity} x ${menu[item]} = ${cost}')
    total_cost += cost

st.write(f'Total: ${total_cost}')