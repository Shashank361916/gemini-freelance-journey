import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor, create_tool_calling_agent

# Import your custom tools
from inquiry_tools import (
    classify_inquiry_tool,
    draft_sales_reply_tool,
    draft_support_reply_tool,
    draft_other_reply_tool
)

# --- Setup ---
load_dotenv('openai.env')
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# --- Agent Assembly ---
print("Assembling the new Tool Calling Agent...")

# 1. The Toolbelt
tools = [
    classify_inquiry_tool, 
    draft_sales_reply_tool, 
    draft_support_reply_tool, 
    draft_other_reply_tool
]

# 2. The Brain
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

# 3. The New Prompt Template
# This is the modern prompt structure for a tool-calling agent
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. You have access to a set of tools."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# 4. Create the New, More Efficient Agent
# We use the standard 'create_tool_calling_agent' function now
agent = create_tool_calling_agent(llm, tools, prompt)

# 5. The Manager
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# --- Run the Agent ---
print("Agent is ready. Giving it an inquiry to handle...")

user_inquiry = "I'm very interested in your enterprise plan. Please can you provide more details and pricing?"

response = agent_executor.invoke({"input": user_inquiry})

print("\n--- Agent's Final Answer ---")
print(response["output"])