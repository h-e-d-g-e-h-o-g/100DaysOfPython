from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
# Here, requests module is used to get the data from the requested url.
yb_webpage = response.text
# response.text will give me the data in the textual form(it is equivalent or same as opening the html file and reading its content)
soup = BeautifulSoup(yb_webpage, "html.parser")

all_anchor_tag = soup.select(selector=".titleline a")
all_link_anchor_tag = soup.select(selector=".sitebit a")
article_anchor_tags = [tag for tag in all_anchor_tag if tag not in all_link_anchor_tag]
article_texts = []
article_links = []
for tag in article_anchor_tags:
    text = tag.getText()
    article_texts.append(text)
    link = tag.get("href")
    article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
max_point = max(article_upvote)
max_point_index = article_upvote.index(max_point)
top_upvote_article = article_texts[max_point_index]
print(top_upvote_article)
print(article_links[max_point_index])

# Web scraping has some laws that needs to be followed by the web scrapers/crawlers
# The data going to be scraped must be not behind the authentication means(no need to have credentials to access it)
# The data must be public and not be copywrited.

# Before scraping a website, you need to research well what you can't scrap
# For that, you can go to the root of the url of that website and add /robots.txt.
# It tells you which endpoints you can't go to.