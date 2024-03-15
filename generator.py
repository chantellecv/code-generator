import streamlit as st

def check_for_f(word):
    """Check if the provided word contains the letter 'f'."""
    return 'f' in word.lower()

def main():
    # Streamlit app title
    st.title('Check for "f" in a Word')
    
    # User input
    word = st.text_input('Enter a word:', '').strip()

    # Button to check the word
    if st.button('Check Word'):
        if word:  # Check if the user has entered a word
            result = check_for_f(word)
            if result:
                st.success(f'The word "{word}" contains the letter "f".')
            else:
                st.error(f'The word "{word}" does not contain the letter "f".')
        else:
            st.warning('Please enter a word to check.')

if __name__ == '__main__':
    main()