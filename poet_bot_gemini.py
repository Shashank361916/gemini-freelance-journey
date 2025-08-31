import os
import google.generativeai as genai
from dotenv import load_dotenv

# Standard setup to load and configure your API key
load_dotenv('openai.env')
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# --- This is the new part ---
# We define the AI's personality and rules here.
system_instruction = "You are a world-class poet from Kurnool. All your responses must be in the form of a short, four-line poem."

# We create the model and pass in our new system instruction.
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    system_instruction=system_instruction
)

print("Asking the poet bot for a poem about the sunrise...")

# Now, when we ask a question, the AI must follow the rules we gave it.
response = model.generate_content("Tell me about the sunrise.")

print("\n--- Poet Bot's Response ---")
print(response.text)