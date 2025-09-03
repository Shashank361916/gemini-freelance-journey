from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

print("Loading and splitting the document...")

loader = PyPDFLoader("document.pdf")
docs = loader.load()

# This creates our "chef's knife"
# chunk_size is the max characters per chunk
# chunk_overlap keeps some text between chunks for context
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

# This performs the split
splits = text_splitter.split_documents(docs)

print(f"The document was split into {len(splits)} chunks.")
print("\n--- Content of the first chunk: ---")
print(splits[0].page_content)