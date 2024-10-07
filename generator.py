Python
import streamlit as st
import os

def create_christmas_tree(num_of_stars):
    result = ""
    for i in range(num_of_stars):
        if i < num_of_stars // 2:
            result += "*" * (num_of_stars - i) + "\n"
        elif i > num_of_stars // 2 - 1:
            result += "*" * (i - num_of_stars // 2 + 1) + "\n"
        else:
            result += "*" + "\n"
    return result

def display_christmas_tree(num_of_stars):
    st.title("Christmas Tree Generator")
    st.write("Enter the number of stars on your Christmas Tree:")
    num_of_stars = int(st.text_input("") or 0)
    if num_of_stars > 0:
        st.write(create_christmas_tree(num_of_stars))
    else:
        st.write("Error: Please enter a positive number.")

if __name__ == "__main__":
    display_christmas_tree(0)