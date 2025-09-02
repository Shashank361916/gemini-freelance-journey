import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser

# --- Setup ---
load_dotenv('openai.env')
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# --- Chain Components ---
output_parser = CommaSeparatedListOutputParser()
format_instructions = output_parser.get_format_instructions()

prompt_template = """
You are a YouTube content strategist.
Generate a list of 5 creative and engaging video ideas for the following topic: {topic}.
{format_instructions}
"""

prompt = ChatPromptTemplate.from_template(prompt_template)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# --- The Chain ---
chain = prompt | llm | output_parser

# --- Run the Chain ---
print("Running YouTube Assistant...")
topic = "learning Python for AI"
video_ideas = chain.invoke({"topic": topic, "format_instructions": format_instructions})

print(f"\nHere are 5 video ideas for a YouTube channel about '{topic}':")
for i, idea in enumerate(video_ideas):
    print(f"{i+1}. {idea.strip()}")