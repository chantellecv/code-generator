import streamlit as st

def check_if_odd(num):
    return num % 2 != 0

def main():
    st.title("Is a number odd?")
    
    num = st.number_input("Enter a number:")
    
    if st.button("Check if odd"):
        is_odd = check_if_odd(num)
        if is_odd:
            st.write(f"{num} is an odd number.")
        else:
            st.write(f"{num} is an even number.")

if __name__ == "__main__":
    main()