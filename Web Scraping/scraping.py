from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all("td", class_="title")
article_texts = []
article_links = []
article_scores = []
for article in articles:
    text = article.select_one(".titleline a")

    if text:
        article_texts.append(text.get_text(strip=True))
        article_links.append(text["href"])
scores = soup.find_all("td", class_="subtext")
for score_ in scores:
    score = score_.select_one(".score")
    text_score = score.get_text(strip=True)
    numbers = "".join(filter(str.isdigit, text_score))
    article_scores.append(int(numbers))

index= article_scores.index(max(article_scores))

print(article_texts[index])
print(article_links[index])
print(article_scores[index])