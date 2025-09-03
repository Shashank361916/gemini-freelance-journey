import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv('openai.env')
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

print("Starting the vector store creation process...")

# 1. Load the document
loader = PyPDFLoader("document.pdf")
docs = loader.load()
print(f"Loaded {len(docs)} pages from the document.")

# 2. Split the text into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
print(f"Split the document into {len(splits)} chunks.")

# 3. Create the embedding model
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# 4. Create the vector store using FAISS
print("Creating embeddings and building the FAISS vector store...")
vector_store = FAISS.from_documents(splits, embedding=embeddings)
print("Vector store created.")

# 5. Save the vector store locally
# This will create a folder named "faiss_index" in your project directory
vector_store.save_local("faiss_index")
print("Vector store saved locally to the 'faiss_index' folder.")