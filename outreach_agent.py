import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor, create_tool_calling_agent

# Import your new custom tool
from research_tools import scrape_website_tool

# --- Setup ---
load_dotenv('openai.env')
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# --- Agent Assembly ---
print("Assembling the Outreach Agent...")

# 1. The Toolbelt: Give the agent its web scraping tool
tools = [scrape_website_tool]

# 2. The Brain
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

# 3. The Prompt Template (Job Description)
prompt = ChatPromptTemplate.from_messages([
    ("system", """
    You are an expert at writing personalized outreach messages.
    Your goal is to read the content of a website and draft a short, personalized email to the person or company.
    The email should mention a specific, interesting point from the website content to show you've done your research.
    """),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# 4. Create the Agent
agent = create_tool_calling_agent(llm, tools, prompt)

# 5. The Manager
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# --- Run the Agent ---
print("Agent is ready. Giving it a research task...")

task = """
Please visit the website https://quotes.toscrape.com/author/Albert-Einstein 
and write a short, personalized outreach email to Albert Einstein, mentioning one of his quotes from the page.
"""

response = agent_executor.invoke({"input": task})

print("\n--- Agent's Final Answer ---")
print(response["output"])