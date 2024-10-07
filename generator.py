import streamlit as st
from typing import str

def generate_christmas_tree(num_stars: int) -> str:
    tree = ""
    for i in range(num_stars):
        tree += "*" * (i + 1) + "\n"
    tree += "|" + " " * (num_stars - 1) + "|\n"
    tree += "|_______|\n"
    return tree

def main():
    st.title("Christmas Tree Generator")
    num_stars = st.number_input("Enter the number of stars:", 1, 20)
    st.write("---Generated Christmas Tree---")
    st.write(generate_christmas_tree(num_stars))

if __name__ == "__main__":
    main()