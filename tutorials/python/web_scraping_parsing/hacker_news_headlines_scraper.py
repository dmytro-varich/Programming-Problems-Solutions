import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    headlines = soup.find_all('span', class_='titleline')

    for index, headline in enumerate(headlines, start=1):
        print(f"{index}. {headline.get_text()}")
else: 
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
