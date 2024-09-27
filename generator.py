import streamlit as st

def main():
    st.title('Is it odd or even???lllll??')

    num = st.number_input('Enter a number:')

    if num % 2 != 0:
        st.write(f'{num} is an odd number')
    else:
        st.write(f'{num} is an even number')

if __name__ == '__main__':
    main()