import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv('openai.env')
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# The Model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# The Prompt Template with two variables
template = """
You are an expert copywriter. Write a short, exciting product description for a product with the following details:
Product Name: {product_name}
Key Features: {features}
"""
prompt = ChatPromptTemplate.from_template(template)

# The Output Parser
output_parser = StrOutputParser()

# The Chain
chain = prompt | llm | output_parser

# Running the chain with two input variables
print("Generating product description...")
response = chain.invoke({
    "product_name": "Galaxy Glow Lamp",
    "features": "Projects realistic stars and nebulae, has 16 color modes, bluetooth speaker"
})

print(response)