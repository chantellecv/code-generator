import streamlit as st
import time

# Function to draw the bouncing ball
def draw_ball(position):
    width = 20  # Width of the animation area
    animation_area = [' '] * width  # Initialize animation area with blank spaces
    animation_area[position] = 'O'  # Place the ball at the current position
    return ''.join(animation_area)  # Convert the list to a string

# Streamlit app
def main():
    st.title('Bouncing Ball ASCII Animation')

    position = 0  # Initial position of the ball
    direction = 1  # Initial direction of the ball movement (1 for right, -1 for left)
    animation_speed = 0.1  # Controls the speed of the animation

    # Placeholder for the animation
    animation_placeholder = st.empty()

    while True:
        # Display the current frame
        animation_placeholder.text(draw_ball(position))

        # Update the position for the next frame
        position += direction

        # Change direction if we hit a wall
        if position == 0 or position == 19:
            direction *= -1

        # Control the speed of the animation
        time.sleep(animation_speed)

if __name__ == '__main__':
    main()