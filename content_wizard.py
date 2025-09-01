import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# --- Standard Setup: Load API Key ---
# This is the same logic from your scripts last week
load_dotenv('openai.env')
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# --- The Web App Interface (Using Streamlit "Lego Bricks") ---

# Set a title for the app
st.title("✒️ The Content Wizard")
st.subheader("Your AI assistant for text analysis.")

# Create a text area for the user to paste their article
article_text = st.text_area("Paste your article here to get started:", height=200)

# Create a button to trigger the analysis
if st.button("Generate Insights"):
    # Check if the user has pasted any text
    if article_text:
        # Show a temporary message while the AI is working
        with st.spinner("The Wizard is thinking..."):

            # --- The AI Part (Using Gemini logic) ---

            # Create the Gemini model
            model = genai.GenerativeModel('gemini-1.5-flash')

            # Create a detailed prompt telling the AI what to do
            prompt = f"""
            You are a professional content analyst. Please analyze the following article and provide these three things:
            1.  **Summary:** A concise, one-paragraph summary.
            2.  **Key Bullet Points:** Five key bullet points that capture the main ideas.
            3.  **Catchy Headline:** One catchy, attention-grabbing headline for this article.

            Here is the article:
            ---
            {article_text}
            """

            # Call the AI to get the response
            response = model.generate_content(prompt)

            # --- Display the Result ---
            st.subheader("Here are your insights:")
            # st.markdown() is great for displaying formatted text
            st.markdown(response.text)
    else:
        # Show a warning if the user clicks the button without pasting text
        st.warning("Please paste an article first.")