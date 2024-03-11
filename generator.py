import streamlit as st

def main():
    st.title("Sum of Two Integers App")
    
    # Collect user input
    num1 = st.number_input("Enter the first integer:")
    num2 = st.number_input("Enter the second integer:")
    
    # Calculate the sum
    result = num1 + num2
    
    # Display the result
    st.write(f"The sum of {num1} and {num2} is: {result}")

if __name__ == '__main__':
    main()