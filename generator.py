import streamlit as st

# Function to check if the number is prime
def is_prime(n):
    # Prime numbers must be greater than 1
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Streamlit app
def main():
    st.title("Prime Number Checker")
    
    # User input
    number = st.number_input("Enter a number", min_value=1, step=1, format='%d')
    
    # Button to check the number
    if st.button("Check Number"):
        result = is_prime(number)
     
        if result:
            st.success(f"{number} is a prime number!")
        else:
            st.error(f"{number} is not a prime number.")

if __name__ == "__main__":
    main()