## GitHub Star Scraper

We're going to scrape [https://github.com](https://github.com), using [`requests`](https://requests.readthedocs.io/en/latest/) and [`Beautiful Soup`](https://beautiful-soup-4.readthedocs.io/en/latest/). Our goal is to get, for a given GitHub `username`, like, for example, [https://github.com/google](https://github.com/google), a list of repositories with their GitHub-assigned programming language as well as the number of stars a repository has.

This sub-project has two scrapers:

1. __star scraper__: It hits the `repositories` tab of a user or an organization and then scrapes the number of stars each repository has.

2. __profile scraper__: It hits the public profile page of a user and gets the linked emails and other links provided by that user. Email can be scraped only if logged in.
