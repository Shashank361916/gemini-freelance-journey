import requests
from bs4 import BeautifulSoup

# The URL of the website we want to scrape
url = "https://quotes.toscrape.com/" # A safe website designed for scraping practice

print(f"Scraping data from: {url}")

# 1. Fetch the website's content
response = requests.get(url)

# 2. Parse the HTML with Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# 3. Find a specific HTML element
# The title of a webpage is inside a <title> tag
title = soup.find('title').text

print("\n--- Found the following information ---")
print(f"Website Title: {title}")