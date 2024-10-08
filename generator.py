import streamlit as st

def check_if_even(num):
    return num % 2 == 0

def main():
    st.title("Is a number even???")
    
    num = st.number_input("Enter a number:")
    
    if st.button("Check if even"):
        is_even = check_if_even(num)
        if is_even:
            st.write(f"{num} is an even number.")
        else:
            st.write(f"{num} is an odd number.")

if __name__ == "__main__":
    main()