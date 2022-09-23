from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com")

soup = BeautifulSoup(response.text, "html.parser")

article_tags = soup.find_all(name="a", class_="titlelink")
scores = soup.find_all(name="span", class_="score")

article_links = []
article_texts = []
article_upvotes = []

for article_tag in article_tags:

    article_text = article_tag.getText()
    article_link = article_tag.get("href")

    article_texts.append(article_text)
    article_links.append(article_link)


for score in scores:
    up_votes = int(score.text.split(" ")[0])
    article_upvotes.append(up_votes)

max_index = article_upvotes.index(max(article_upvotes))

print("Article with highest up votes")
print(f"Text: {article_texts[max_index]}")
print(f"Link: {article_links[max_index]}")
print(f"Up votes: {article_upvotes[max_index]}")
