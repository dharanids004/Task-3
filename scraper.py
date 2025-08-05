import requests
from bs4 import BeautifulSoup

# URL of the news site
url = 'https://www.bbc.com/news'

# Set User-Agent to prevent blocking
headers = {
    'User-Agent': 'Mozilla/5.0'
}

# Fetch the content
response = requests.get(url, headers=headers)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract headlines (you can change 'h3' based on site)
headlines = soup.find_all(['h1', 'h2', 'h3'])

# Write to a text file
with open('headlines.txt', 'w', encoding='utf-8') as f:
    for i, headline in enumerate(headlines, 1):
        text = headline.get_text(strip=True)
        if text:
            f.write(f"{i}. {text}\n")

print("Headlines saved to headlines.txt")