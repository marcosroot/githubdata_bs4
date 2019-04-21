from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input("enter url: ")
res = urlopen(url)
bs = BeautifulSoup(res, "html.parser")

owner = bs.find("a", {"rel": "author"}).get_text()
name = bs.find("a", {"data-pjax": "#js-repo-pjax-container"}).get_text()
description = bs.find("span", {"itemprop": "about"}).get_text().strip()
stars = bs.find("a", {"class": "social-count js-social-count"}).get_text().strip()
commits = bs.find("span", {"class": "num text-emphasized"}).get_text().strip()
last_commit = bs.find("relative-time").get_text().strip()

print(f"{name} by {owner}")
print(f"Description: {description}")
print(stars, "stars")
print(commits, "commits")
print(f"Last commit in {last_commit}")
