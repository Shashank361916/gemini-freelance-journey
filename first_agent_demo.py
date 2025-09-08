import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from datetime import date
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor

# --- Setup and Tool Definition ---
load_dotenv('openai.env')
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

@tool
def get_current_date() -> str:
    """
    Returns the current date in YYYY-MM-DD format.
    Use this whenever you are asked about today's date.
    """
    return str(date.today())

# --- Agent Assembly ---
print("Assembling the agent...")

# 1. The Toolbelt: A list of all tools the agent can use
tools = [get_current_date]

# 2. The Brain: The LLM that will do the reasoning
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

# 3. The Job Description (Prompt): A pre-made prompt from LangChain Hub
prompt = hub.pull("hwchase17/react")

# 4. Create the Agent
agent = create_react_agent(llm, tools, prompt)

# 5. The Manager: The Agent Executor runs the agent's thought loop
# verbose=True lets us see the agent's thoughts
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# --- Run the Agent ---
print("Running the agent...")
question = "What is today's date?"
response = agent_executor.invoke({"input": question})

print("\n--- Final Answer ---")
print(response["output"])