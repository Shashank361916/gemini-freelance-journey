import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# --- Setup ---
load_dotenv('openai.env')
# Note: LangChain uses a slightly different way to set the key
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# --- Building the Chain ---

# 1. The Model (Our "water heater")
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# 2. The Prompt Template (Our "form letter")
prompt = ChatPromptTemplate.from_template(
    "You are a helpful assistant. Tell me a fun fact about {topic}."
)

# 3. The Output Parser (Formats the final output as simple text)
output_parser = StrOutputParser()

# 4. The Chain (Connecting the pipes)
# We use the pipe symbol | to connect the components
chain = prompt | llm | output_parser

# --- Running the Chain ---
print("Running the LangChain chain...")
# The .invoke() method runs the chain. The input is a dictionary
# where the key matches the variable in our prompt template.
response = chain.invoke({"topic": "the moon"})

print(response)