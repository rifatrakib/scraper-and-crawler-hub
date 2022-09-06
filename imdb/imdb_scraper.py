import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


url = "http://www.imdb.com/title/tt0944947/episodes"
episodes = []
ratings = []

# go over seasons 1 to 8
for season in range(1, 9):
    r = requests.get(url, params={"season": season})
    html_soup = BeautifulSoup(r.text, "html.parser")
    
    items = html_soup.find("div", class_="eplist")
    for epnr, div in enumerate(items.find_all("div", recursive=False)):
        episode = f"{season}.{epnr+1}"
        rating = float(div.find(class_="ipl-rating-star__rating").get_text(strip=True))
        print(f"{episode=}\t\t{rating=}")
        episodes.append(episode)
        ratings.append(rating)

positions = [a * 2 for a in range(len(ratings))]
episodes = [
    "S" + ep.split(".")[0] if int(ep.split(".")[1]) == 1 else "" for ep in episodes
]

plt.figure()
plt.bar(positions, ratings, align="center")
plt.xticks(positions, episodes)
plt.show()
