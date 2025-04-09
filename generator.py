```python
import streamlit as st

def main():
    st.title('Simple Game App')
    
    user_input = st.text_input('Enter your name:')
    
    if st.button('Start Game'):
        st.success(f'Welcome {user_input}! Let the game begin.')
        
        # Add your game logic here
        
if __name__ == '__main__':
    main()
```