import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

# --- Setup ---
load_dotenv('openai.env')
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")


# --- The Modern RAG Chain ---
def create_rag_chain():
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)

    # <<< FIX #1 IS HERE! Change {question} to {input}
    prompt_template = """
    You are a helpful AI assistant. Answer the user's question based ONLY on the following context.
    If the information is not in the context, say "I couldn't find the answer in the provided document."

    CONTEXT:
    {context}

    QUESTION:
    {input}

    ANSWER:
    """
    prompt = ChatPromptTemplate.from_template(prompt_template)

    document_chain = create_stuff_documents_chain(llm, prompt)

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    retriever = vector_store.as_retriever()

    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    
    return retrieval_chain


# --- The Streamlit App Interface ---

st.set_page_config(page_title="Knowledge Base Bot 📚", layout="wide")
st.title("Chat with Your PDF 📚")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! Ask me anything about your document."}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_question := st.chat_input("Ask a question about your PDF:"):
    st.session_state.messages.append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.markdown(user_question)

    with st.spinner("Thinking..."):
        chain = create_rag_chain()
        
        # <<< FIX #2 IS HERE! Change "question" back to "input"
        response = chain.invoke({"input": user_question})
        
        final_answer = response['answer']

    st.session_state.messages.append({"role": "assistant", "content": final_answer})
    with st.chat_message("assistant"):
        st.markdown(final_answer)