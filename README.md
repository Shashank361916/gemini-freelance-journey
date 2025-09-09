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
- Python
- Streamlit (for the web interface)
- Google Gemini (as the core LLM)
- LangChain (for the RAG framework)
- FAISS (for the local vector store)

### How to Get it Running

Follow the instructions in the `knowledge_base_bot.py` and `create_vector_store.py` files. You will need to add a `document.pdf` and run the `create_vector_store.py` script once before starting the Streamlit app.

---

## Project #2: Automated Inquiry Agent 🤖

This project was about making AI take action. I built an autonomous agent that can read incoming customer messages, figure out what they're about (like a sales question or a support ticket), and then draft a suitable reply. This is a huge step towards automating real business workflows.

The magic here is the agent's ability to use a "toolbelt" of custom functions to perform its multi-step task without human intervention.

### Agent's Chain of Thought (Example)
!
*(You can see the agent's reasoning process in this screenshot from my terminal.)*

### Tech Stack
- LangChain Agents (AgentExecutor, `create_tool_calling_agent`)
- Custom Tools for multi-step reasoning
- Google Gemini 1.5 Flash

### How to Run
Run the agent from your terminal with `python inquiry_agent.py`.

---

## Project #3: Personalized Outreach Assistant 🌐

The next superpower I wanted to give my agents was access to the live internet. This project features a research agent that can browse a website, extract key information, and then use that information to complete a task.

For this demonstration, the agent visits a webpage, understands its content, and drafts a personalized outreach email that references specific details from the page, making the message far more effective than a generic template.

### Agent's Reasoning and Output
!
*(Here's a look at the agent scraping the website and drafting the final email.)*

### Tech Stack
- LangChain Agents
- Custom Web Scraping Tool
- **Beautiful Soup** & **Requests** (for web scraping)
- Google Gemini 1.5 Flash

### How to Run
Run the agent from your terminal with `python outreach_agent.py`. The task and URL can be changed directly within the script.
