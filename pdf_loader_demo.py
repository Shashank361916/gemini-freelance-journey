from langchain_community.document_loaders import PyPDFLoader

print("Loading PDF...")

# This creates the "can opener" for our PDF
loader = PyPDFLoader("document.pdf")

# This loads the document and splits it by page
pages = loader.load_and_split()

print(f"Your document has {len(pages)} pages.")
print("\n--- Content of the first page: ---")
# Each 'page' object has the content and metadata (like the page number)
print(pages[0].page_content)