# My AI Freelance Journey 🚀

Hello! My name is Shashank, and this repository is a living journal of my journey to become a freelance AI Agent developer. I'm based in Kurnool, India, and I'm passionate about building practical, intelligent solutions for real-world business problems.

This is where I'm documenting my projects, from the first line of code to the final, polished application. Feel free to explore and see what I'm building!

---

## Project #1: Knowledge Base Bot 📚

Have you ever wished you could just *talk* to your documents? That's the problem I set out to solve with this project. It's a web app that lets you upload a PDF and then ask it questions, getting accurate answers based only on the document's content.

This was my first major project to master **Retrieval-Augmented Generation (RAG)**, a key technique for building AI that can reason about private data.

### Screenshot


*(Here's a quick look at the app in action!)*

### Tech Stack
- **Python**
- **Streamlit** (for the web interface)
- **Google Gemini** (as the core LLM)
- **LangChain** (for the RAG framework)
- **FAISS** (for the local vector store)

### How to Get it Running

**1. Clone the Repository**
```bash
git clone [https://github.com/Your-Username/gemini-freelance-journey.git](https://github.com/Your-Username/gemini-freelance-journey.git)
cd gemini-freelance-journey
2. Set Up Your Environment

Bash

# Create and activate a virtual environment
python -m venv .venv
# On Windows, use `.venv\Scripts\activate`
.venv\Scripts\activate  

# Install all the required libraries
pip install -r requirements.txt
3. Add Your API Key

Create a file named .env.

Inside, add your Google API key:

GOOGLE_API_KEY="YOUR_API_KEY_HERE"
4. Add Your Document

Find a PDF you want to chat with and place it in the project folder.

Rename it to document.pdf.

5. Create the "Brain"

This command processes your PDF and creates a searchable vector store. You only need to run this once per document.

Bash

python create_vector_store.py
6. Run the App!

Now, start the chat application.

Bash

streamlit run knowledge_base_bot.py
Project #2: Automated Inquiry Agent 🤖
This project was about making AI take action. I built an autonomous agent that can read incoming customer messages, figure out what they're about (like a sales question or a support ticket), and then draft a suitable reply. This is a huge step towards automating real business workflows.

The magic here is the agent's ability to use a "toolbelt" of custom functions to perform its multi-step task without human intervention.

Agent's Chain of Thought (Example)
!
(You can see the agent's reasoning process in this screenshot from my terminal.)

Tech Stack
LangChain Agents (AgentExecutor, create_tool_calling_agent)

Custom Tools for multi-step reasoning

Google Gemini 1.5 Flash

How to Run
Make sure your environment is set up and libraries from requirements.txt are installed.

Ensure your .env file is configured with your GOOGLE_API_KEY.

Run the agent from your terminal:

Bash

python inquiry_agent.py
