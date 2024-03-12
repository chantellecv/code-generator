import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from noise import pnoise2

def generate_perlin_noise(width, height, scale, octaves):
    """
    Generate a 2D numpy array of perlin noise.
    """
    noise = np.zeros((width, height))
    for i in range(width):
        for j in range(height):
            noise[i][j] = pnoise2(i / scale, 
                                  j / scale, 
                                  octaves=octaves)
    return noise

def plot_noise(noise_map, colormap):
    """
    Plot the generated perlin noise using matplotlib.
    """
    plt.figure(figsize=(10, 10))
    plt.imshow(noise_map, cmap=colormap)
    plt.axis('off')
    st.pyplot(plt)

def main():
    st.title("Abstract Art Generator")
    
    with st.sidebar:
        width = st.number_input("Image width", min_value=100, max_value=1000, value=500)
        height = st.number_input("Image height", min_value=100, max_value=1000, value=500)
        scale = st.slider("Scale", min_value=10, max_value=100, value=50)
        octaves = st.slider("Complexity (Octaves)", min_value=1, max_value=10, value=5)
        colormap = st.selectbox("Color map", options=plt.colormaps(), index=plt.colormaps().index('magma'))

    st.subheader("Generated Art")
    
    if st.button("Generate"):
        noise_map = generate_perlin_noise(width, height, scale, octaves)
        plot_noise(noise_map, colormap)

if __name__ == "__main__":
    main()