import requests
from bs4 import BeautifulSoup
from langchain_core.tools import tool

@tool
def scrape_website_tool(url: str) -> str:
    """
    Scrapes the main text content from a given website URL.
    Use this tool to find information about a person, company, or topic.
    The input to this tool must be a valid URL.
    """
    try:
        print(f"--- Scraping content from {url} ---")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the main content of the page (this works for many articles/blogs)
        # You can also target specific tags like soup.find_all('p') for paragraphs
        main_content = soup.find('body')
        if main_content:
            # Clean up the text by removing extra whitespace
            return " ".join(main_content.text.split())
        else:
            return "Could not find the main content of the page."
    except Exception as e:
        return f"An error occurred: {e}"

# Test the tool
if __name__ == "__main__":
    test_url = "https://quotes.toscrape.com/"
    scraped_data = scrape_website_tool.invoke({"url": test_url})
    print("\n--- Scraped Data ---")
    # We'll print only the first 500 characters for brevity
    print(scraped_data[:500] + "...")