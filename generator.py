import streamlit as st
import time

# ASCII Art Frames
frames = [
    """
    Frame 1
    Your ASCII Art Here
    """,
    """
    Frame 2
    Your ASCII Art Here
    """,
    """
    Frame 3
    Your ASCII Art Here
    """,
    # Add more frames as needed
]

st.title('Simple ASCII Art Animation')

# Loop to animate
while True:
    for frame in frames:
        # Clear previous frame
        st.empty()
        st.code(frame, language='')
        # Adjust time.sleep to control the speed of your animation
        time.sleep(0.5)