import streamlit as st
import math

st.title("Prime Number Checker")
number = int(st.number_input("Enter a number", key="num_input"))

if st.button("Check Prime", key="check_prime"):
    if number > 1:
        if number <= 3:
            is_prime = True
        else:
            is_prime = False
            for i in range(2,int(math.sqrt(number)) + 1):
                if (number % i) == 0:
                    is_prime = False
                    break
        if is_prime:
            st.write(number,"is a prime number")
        else:
            st.write(number,"is not a prime number")
    else:
        st.write("Please enter a number greater than 1")