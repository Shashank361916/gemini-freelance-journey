import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv('openai.env')
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# This creates the embedding model object
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

print("Creating an embedding for a single piece of text...")
# Get the embedding for one sentence
result_vector = embeddings.embed_query("King")
print(f"The word 'King' is represented by a list of {len(result_vector)} numbers.")
print(f"The first 5 numbers are: {result_vector[:5]}")

print("\nCreating embeddings for multiple pieces of text...")
# Get embeddings for a list of sentences
result_vectors = embeddings.embed_documents(["Apple", "Orange", "Car"])
print(f"We got back {len(result_vectors)} lists of numbers, one for each word.")