import re, requests
from bs4 import BeautifulSoup

HOST = 'https://en.wikipedia.org'
EXCLUDING_NAMESPACES = re.compile(f"^/wiki/(?!\w+:)")

def is_string_valid(s: str) -> bool:
    return not any(exception in s for exception in LST_EXCEPTION)

def wikiscraping(url: str) -> dict:
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    div_container = soup.find("div", id="bodyContent")
    a_elements = div_container.find_all("a", href=EXCLUDING_NAMESPACES)
    
    return {a_element.get('title'): HOST + a_element.get('href') for a_element in a_elements}
