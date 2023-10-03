# BeutifulSoup4 simple example

import requests
from bs4 import BeautifulSoup

# Set the headers like we are a browser,
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

url = "https://quotes.toscrape.com/"

# Make a request
page = requests.get(url, headers=header)

# Parse the HTML content
soup = BeautifulSoup(page.content, 'html.parser')

# Loop through each quote block and extract quote and author
for quote_block in soup.find_all('div', class_='quote'):
    quote_text = quote_block.find('span', class_='text').text
    author_name = quote_block.find('small', class_='author').text
    # Add row to the table
    print(f"{quote_text} - {author_name}")

