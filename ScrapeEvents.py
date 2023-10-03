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

# If pagecontent is not None, continue
if pagecontent:
    # Find all list items within pagecontent
    items = pagecontent.find_all('li', class_='sv-channel-item')

    for item in items:
        # Initialize default values for title and date
        title = "No title found"
        date = "No date found"
        
        # Try to find and extract title and date
        title_tag = item.find('span', class_='sol-article-item-heading')
        date_tag = item.find('span', class_='sol-article-item-fulldate')
        
        if title_tag:
            title = title_tag.text
        
        if date_tag:
            date = date_tag.text
        
        # Print the title and date
        print(f'Title: {title}')
        print(f'Date: {date}')
        print(f'{"-"*50}')

