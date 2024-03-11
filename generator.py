import streamlit as st

def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert string to lowercase and remove spaces
    return s == s[::-1]

def main():
    st.title("Palindrome Checker")
    user_input = st.text_input("Enter a string:")
    
    if st.button("Check if Palindrome"):
        if is_palindrome(user_input):
            st.write(f"'{user_input}' is a palindrome!")
        else:
            st.write(f"'{user_input}' is not a palindrome.")

if __name__ == "__main__":
    main()