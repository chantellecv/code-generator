import streamlit as st
import textwrap

def generate_christmas_tree(n_stars):
    stars = ''
    dots = ''
    for i in range(n_stars):
        stars += '*' * (i + 1) + '\n'
    for i in range(n_stars - 2, -1, -1):
        dots += '*' * (i + 1) + '\n'
    return stars + dots

def main():
    st.title("Christmas Tree Generator")
    n_stars = st.slider("Enter the number of stars:", 1, 20, 5)
    tree = generate_christmas_tree(n_stars)
    lines = tree.splitlines()
    st.markdown("".join(map(lambda line: f"{' ' * 10} {line}", lines)))
    st.markdown("{" + ("{" * 9) + "}")

if __name__ == "__main__":
    main()