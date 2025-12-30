from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(markup=yc_webpage, features="html.parser")

articles = []
article_links = []
article_upvotes = []

article_rows = soup.find_all("tr", class_="athing")

for row in article_rows:
    title_tag = row.find("span", class_="titleline").find("a")

    articles.append(title_tag.getText())
    article_links.append(title_tag.get("href"))

    subtext = row.find_next_sibling("tr").find("td", class_="subtext")
    score_tag = subtext.find("span", class_="score")

    if score_tag:
        article_upvotes.append(int(score_tag.getText().split()[0]))
    else:
        article_upvotes.append(0)

largest_no = max(article_upvotes)
largest_index = article_upvotes.index(largest_no)

print(
    f"The Most popular article at the moment:\n"
    f"Article: {articles[largest_index]}\n"
    f"Link: {article_links[largest_index]}\n"
    f"Points: {largest_no}"
)

'''Some Web Scrapings are unethical and you should check before Scraping.
To check what not to do with the website, add robots.txt beside the website url
ex: https://news.ycombinator.com/robots.txt'''
