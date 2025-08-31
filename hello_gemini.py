import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load the environment file that contains your API key
load_dotenv('openai.env')

# Configure the library with your Google API key
# Notice we are now getting the "GOOGLE_API_KEY"
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

print("Asking the Gemini AI a question...")

# Create the model
# gemini-1.5-flash is a great, fast, and free model to start with
model = genai.GenerativeModel('gemini-1.5-flash')

# Send the prompt to the AI
response = model.generate_content("Say 'Hello, I am ready to start learning!' in a confident voice.")

# Print the AI's response
print("AI says: " + response.text)