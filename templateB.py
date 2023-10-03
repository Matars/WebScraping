import requests
from bs4 import BeautifulSoup

# Set the headers like we are a browser,
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

url = "https://www.vaxjo.se/sidor/se-och-gora/nyheter---se-och-gora.html"

# Make a request
page = requests.get(url, headers=header)

# Parse the HTML content
soup = BeautifulSoup(page.content, 'html.parser')

# find pagecontent class
pagecontent = soup.find('ul', class_='sv-defaultlist')
