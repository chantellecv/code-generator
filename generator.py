import streamlit as st

def calculate_difference(num1, num2):
    """Calculate the difference between two numbers."""
    return abs(num1 - num2)

def main():
    st.title("Difference Calculator")
    
    # User inputs for the two numbers
    num1 = st.number_input("Enter the first integer:", value=0, format="%d")
    num2 = st.number_input("Enter the second integer:", value=0, format="%d")
    
    # A button to perform the calculation
    if st.button("Calculate Difference"):
        result = calculate_difference(num1, num2)
        st.success(f"The difference between {num1} and {num2} is {result}.")
        
if __name__ == "__main__":
    main()