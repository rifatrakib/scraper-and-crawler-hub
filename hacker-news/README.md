## Hacker News (Scraper)

### Non-API version ([`hacker_news_scraper.py`](https://github.com/rifatrakib/scraper-and-crawler-hub/blob/master/hacker-news/hacker_news_scraper.py))

In this sub-project, we are going to scrape the [`Hacker News`](https://news.ycombinator.com/news) front page, using [`requests`](https://requests.readthedocs.io/en/latest/) and [`Beautiful Soup`](https://beautiful-soup-4.readthedocs.io/en/latest/). Take some time to explore the page if you haven’t heard about it already. Hacker News is a popular aggregator of news articles that `"hackers"` (computer scientists, entrepreneurs, data scientists) find interesting. We'll store the scraped information in a simple Python list of dictionary objects for this sub-project.


### API version ([`hacker_api_scraper.py`](https://github.com/rifatrakib/scraper-and-crawler-hub/blob/master/hacker-news/hacker_api_scraper.py))

[`Hacker News`](https://news.ycombinator.com/news) also offers an API providing structured, JSON-formatted results (see [`https://github.com/HackerNews/API`](https://github.com/HackerNews/API)). Rework the Python code to serve as an API client without relying on [`Beautiful Soup`](https://beautiful-soup-4.readthedocs.io/en/latest/) for HTML parsing.
