# We need these two new lines to load our .env file
import os
from dotenv import load_dotenv

from openai import OpenAI

# This line finds the .env file and loads the variables from it
load_dotenv('openai.env')

# This is the new, secure way to get your API key
# It looks for a variable named OPENAI_API_KEY in your environment (which load_dotenv just set up for you)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("Asking the AI a question...")

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Say 'Hello, I am ready to start learning!' in a confident voice."}
  ]
)

ai_message = response.choices[0].message.content
print("AI says: " + ai_message)