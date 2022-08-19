import requests

articles = []
url = "https://hacker-news.firebaseio.com/v0"
top_stories = requests.get(url + "/topstories.json").json()

for story_id in top_stories:
    story_url = f"{url}/item/{story_id}.json"
    print(f"fetching: {story_url}")
    r = requests.get(story_url)
    story_dict = r.json()
    articles.append(story_dict)

for article in articles:
    print(article)
