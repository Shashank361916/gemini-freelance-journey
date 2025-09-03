import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv('openai.env')
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# 1. Create the embedding model (must be the same one used to create the store)
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# 2. Load the saved vector store from the local folder
print("Loading the local FAISS index...")
vector_store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
print("FAISS index loaded.")

# 3. Create the retriever
# This object knows how to search the vector store
retriever = vector_store.as_retriever()

# 4. Ask a question
question = "Which attribute is most important in a Trustworthy AI system?" # Change this question to be relevant to YOUR PDF
print(f"\nSearching for documents related to: '{question}'")

# 5. Use the retriever to find the relevant documents
relevant_docs = retriever.invoke(question)

# 6. Display the results
print("\n--- Here are the most relevant documents found ---")
for i, doc in enumerate(relevant_docs):
    print(f"--- Document {i+1} ---")
    print(doc.page_content)
    print("\n")