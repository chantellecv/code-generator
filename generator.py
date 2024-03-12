import streamlit as st
from time import sleep

# ASCII Art options
ascii_options = {
    "Rocket": """
       ^
      /^\\
      |-|
      | |
      |N|
      |A|
      |S|
      |A|
     /| |\\
    / | | \\
   |  | |  |
    `-"""-`
    """,
    "Robot": """
     /\\_/\\  
    ( o.o ) 
     > ^ <
    """,
    "Cat": """
     /\_/\  
    ( o.o ) 
     > ^ <
    """
}

def animate_ascii_art(art):
    # The number of spaces increases to simulate movement
    for i in range(20):
        st.write(f"{' ' * i}{art}")
        sleep(0.1)
        st.experimental_rerun()

st.title('Simple ASCII Art Animation')

# Dropdown for ASCII art selection
selected_art = st.selectbox('Choose an ASCII character', options=list(ascii_options.keys()))

# Start animation button
if st.button('Start Animation'):
    animate_ascii_art(ascii_options[selected_art])