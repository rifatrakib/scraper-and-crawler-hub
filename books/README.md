## Book Scraper

We're going to scrape [http://books.toscrape.com](http://books.toscrape.com), using [`requests`](https://requests.readthedocs.io/en/latest/) and [`Beautiful Soup`](https://beautiful-soup-4.readthedocs.io/en/latest/). This page is provided by [`Scrapinghub`](https://www.zyte.com/) as a more realistic scraping playground. Take some time to explore the page. We'll scrape out all the information, that is, for every book, we'll obtain the following for each book:

* title
* image
* price and stock availability
* rating
* product description
* and other product information

We're going to store this information in an `SQLite database`, again using the [`dataset`](https://dataset.readthedocs.io/en/latest/) library. However, this time we’re going to write our program in such a way that it takes into account updates — so that we can run it multiple times without inserting duplicate records in the database.
