from bs4 import BeautifulSoup
import requests
import pandas as pd

movies = []
pageNum = 2
url = f"https://kinogo.by/page/{pageNum}/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
divs = soup.find_all("div", class_="shortstory")
for i in divs:
    title = i.find("h2", "zagolovki").text
    description = i.find("div")