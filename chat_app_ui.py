import streamlit as st

st.title("🤖 Basic Chat UI")

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input from the chat input box at the bottom
if prompt := st.chat_input("What is your question?"):
    # Add user message to session state and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- This is where the AI response will go ---
    # For now, we'll just add a dummy response
    dummy_response = f"You asked: {prompt}"
    st.session_state.messages.append({"role": "assistant", "content": dummy_response})
    with st.chat_message("assistant"):
        st.markdown(dummy_response)