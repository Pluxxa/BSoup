from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

text = soup.find_all("span", class_="text")
author = soup.find_all("small", class_="author")

for i in range(10):
    print(f"Автор текста {text[i].text} - {author[i].text}")
    print()