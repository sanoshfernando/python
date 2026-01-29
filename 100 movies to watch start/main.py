import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
webpage = response.text
soup = BeautifulSoup(webpage,"html.parser")

titles = soup.find_all("h3", class_="title")
topics =[]
for topic in titles:
    topics.append(topic.getText(strip=True))
topics= reversed(topics)

try:
    open("myfile.txt", "x", encoding="utf-8")
except FileExistsError:
    with open("myfile.txt", "w", encoding="utf-8") as f:
        for topic in topics:
            f.write(f"{topic}\n")
