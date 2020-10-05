from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

animes = []
names = []
for el in range(1,248):
    print(el)
    url = f"https://animevost.am/page/{el}/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    animeInfo = soup.find_all("div", class_="shortstory")
    for i in animeInfo:
        anime = {}
        title_div = i.find("div", class_="shortstoryHead")
        image = i.find("img", class_="imgRadius")
        image_url = "https://animevost.am"+image["src"]
        title = title_div.text.rstrip("\n\n")
        table = i.find("table")
        info = table.find_all("p")
        anime["название"] = title
        anime["фотография"] = image_url
        for j in info:
            parts = j.text.split(":")
            if parts[0] != "Режиссёр":
                anime[parts[0]] = parts[1]
        animes.append(anime)
print(animes)
print(names)
print(len(names))
pd = pd.DataFrame(animes)
pd = pd.replace(r'\n\n',' ', regex=True)
pd.to_csv("../RecommendedSystem/data.csv")