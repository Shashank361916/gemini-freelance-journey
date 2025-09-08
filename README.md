\# Project #1: Knowledge Base Bot 📚



A web application that allows you to chat with your PDF documents, built with Streamlit, Google Gemini, and LangChain. This app uses a RAG (Retrieval-Augmented Generation) pipeline to provide accurate answers based on the content of a user-provided PDF.



\## Screenshot



(You can add a screenshot here later by editing the file on GitHub and dragging the image in.)



---



\## Technologies Used

\- Python

\- Streamlit (for the web interface)

\- Google Gemini (as the core LLM)

\- LangChain (for the RAG framework)

\- FAISS (for the vector store)



---



\## How to Run This Project Locally



Follow these steps to set up and run the project on your own machine.



\*\*1. Clone the Repository\*\*

```bash

git clone \[https://github.com/Your-Username/gemini-freelance-journey.git](https://github.com/Your-Username/gemini-freelance-journey.git)

cd gemini-freelance-journey

(.venv) C:\Users\MSI\Documents\ai-freelance-journey>python inquiry_agent.py
Assembling the new Tool Calling Agent...
Agent is ready. Giving it an inquiry to handle...


> Entering new AgentExecutor chain...

Invoking: `classify_inquiry_tool` with `{'inquiry': "I'm very interested in your enterprise plan. Please can you provide more details and pricing?"}`


sales
Invoking: `draft_sales_reply_tool` with `{'inquiry': "I'm very interested in your enterprise plan. Please can you provide more details and pricing?"}`


Thank you for your interest in our enterprise plan. We appreciate you reaching out.  A sales representative will be in contact with you shortly to discuss your needs and provide you with detailed information and pricing.Thank you for your interest in our enterprise plan. We appreciate you reaching out.  A sales representative will be in contact with you shortly to discuss your needs and provide you with detailed information and pricing.

> Finished chain.

--- Agent's Final Answer ---
Thank you for your interest in our enterprise plan. We appreciate you reaching out.  A sales representative will be in contact with you shortly to discuss your needs and provide you with detailed information and pricing.
