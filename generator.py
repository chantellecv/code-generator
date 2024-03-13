import streamlit as st

# Function to check if the number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Streamlit app
def main():
    # App title
    st.title("Prime Number Checker")

    # Number input from user
    number = st.number_input("Enter a number", min_value=1, value=1, step=1)

    # Button to check if the number is prime
    if st.button("Check if Prime"):
        # Using the is_prime function to check the number
        if is_prime(number):
            st.success(f"{number} is a Prime Number!")
        else:
            st.error(f"{number} is not a Prime Number.")

# Run the app
if __name__ == "__main__":
    main()