import streamlit as st

def main():
    # Set the title of the app
    st.title("Christmas Tree Generator")

    # Add a header to the app
    st.header("Enter the number of stars to create a Christmas tree:")

    # Create a slider to input the number of stars
    num_stars = st.slider("Number of Stars", 1, 100, 25)

    # Create the Christmas tree
    tree = ""
    for i in range(num_stars):
        tree += "*" * (num_stars - i) + "\n"
    for i in range(num_stars - 2, -1, -1):
        tree += "*" * i + "\n"

    # Display the Christmas tree
    st.markdown(tree)

if __name__ == "__main__":
    main()