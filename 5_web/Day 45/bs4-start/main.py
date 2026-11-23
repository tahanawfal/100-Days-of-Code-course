from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page  = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_texts = []
article_links = []

articles = soup.find_all(name="span", class_="titleline")
for tag in articles:
    text = tag.a.getText()
    article_texts.append(text)
    link  = tag.a.get("href")
    article_links.append(link)

article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]
article_upvotes_digits = [int(value.split(" ")[0]) for value in article_upvotes]

higest_upvote = max(article_upvotes_digits)
index_of = article_upvotes_digits.index(higest_upvote)
print(article_texts[index_of], article_links[index_of], article_upvotes_digits[index_of])