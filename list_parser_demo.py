import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser

load_dotenv('openai.env')
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# 1. Create the Output Parser
output_parser = CommaSeparatedListOutputParser()

# 2. Get the formatting instructions from the parser
format_instructions = output_parser.get_format_instructions()

# 3. Create the prompt template, including the instructions
prompt = ChatPromptTemplate.from_template(
    "List 5 creative names for a new coffee shop in Kurnool.\n{format_instructions}"
)

# 4. The Model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# 5. The Chain (notice the parser is at the end)
chain = prompt | llm | output_parser

# Run the chain
print("Generating coffee shop names...")
response = chain.invoke({"format_instructions": format_instructions})

# The response is now a Python list!
print(response)
print(f"The first suggested name is: {response[0]}")