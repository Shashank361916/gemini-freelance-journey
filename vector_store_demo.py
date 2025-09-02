import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv('openai.env')
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# 1. The text from our "book"
our_documents = [
    "The capital of France is Paris.",
    "Shashank lives in the city of Kurnool.",
    "The currency of Japan is the Yen.",
    "The main language spoken in Andhra Pradesh is Telugu."
]

# 2. The embedding model
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# 3. Create the Vector Store (the "GPS")
# This takes our documents, creates embeddings, and stores them
print("Creating the vector store...")
vector_store = FAISS.from_texts(our_documents, embedding=embeddings)
print("Vector store created.")

# 4. Ask a question
question = "Where does Shashank live?"
print(f"\nSearching for documents related to: '{question}'")

# 5. Perform the search
# This converts the question to an embedding and finds the closest matches
relevant_docs = vector_store.similarity_search(question)

# 6. Show the results
print("\n--- Here is the most relevant document found ---")
print(relevant_docs[0].page_content)