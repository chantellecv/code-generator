import streamlit as st

# Define the menu items with prices
menu = {
    'Burger': 5.99,
    'Pizza': 8.99,
    'Salad': 6.99,
    'Fries': 2.99
}

st.title('Self-Ordering Kiosk App')

# Display the menu to the user
st.write('### Menu:')
for item, price in menu.items():
    st.write(f'- {item}: ${price}')

# Allow users to select items to add to their order
user_order = []
total_price = 0.0

st.write('\n### Select Items to Add to Your Order:')
for item in menu:
    option = st.checkbox(item)
    if option:
        user_order.append(item)
        total_price += menu[item]

st.write('\n### Your Order:')
for item in user_order:
    st.write(f'- {item}')

st.write(f'\n**Total Price:** ${total_price}')

# Allow users to place the order
if st.button('Place Order'):
    st.success('Your order has been placed!')