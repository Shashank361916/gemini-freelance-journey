import os
import google.generativeai as genai
from dotenv import load_dotenv

# This loads your openai.env file
load_dotenv('openai.env')

# This configures the library with your key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# We create the model so we can use its tools
model = genai.GenerativeModel('gemini-1.5-flash')

print("Counting tokens...")

# --- English Example ---
prompt_en = "How many tokens are in this sentence?"
response_en = model.count_tokens(prompt_en)
print(f"The English prompt has: {response_en.total_tokens} tokens.")


# --- Telugu Example ---
prompt_te = "ఈ వాక్యంలో ఎన్ని టోకెన్లు ఉన్నాయి?"
response_te = model.count_tokens(prompt_te)
print(f"The Telugu prompt has: {response_te.total_tokens} tokens.")