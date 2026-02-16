import requests
from bs4 import BeautifulSoup

# Step 1: Define the URL of the news website
url = "https://www.bbc.com/news"

# Step 2: Send HTTP GET request to fetch HTML content
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    print("Successfully fetched the webpage!")
else:
    print("Failed to fetch webpage")
    exit()

# Step 3: Parse HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Extract headlines from <h2> tags
headlines = []

# Extract <title> tag
page_title = soup.title.string.strip()
headlines.append(f"PAGE TITLE: {page_title}")
headlines.append("=" * 50)

# Extract all <h2> tags
for h2 in soup.find_all("h2"):
    text = h2.get_text(strip=True)
    if text:  # Avoid empty tags
        headlines.append(text)

# Step 5: Save headlines to a .txt file
with open("headlines.txt", "w", encoding="utf-8") as file:
    for headline in headlines:
        file.write(headline + "\n")

print("Headlines saved to headlines.txt")
