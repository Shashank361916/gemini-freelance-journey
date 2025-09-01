import streamlit as st

st.title("Interactive App")

# This creates a text box and saves what the user types into the 'name' variable
name = st.text_input("What is your name?")

# This creates a button. The code inside the 'if' block only runs when it's clicked.
if st.button("Say Hello"):
    st.write(f"Hello, {name}! Welcome to your first interactive app.")