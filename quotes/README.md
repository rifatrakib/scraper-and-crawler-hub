We're going to scrape [http://quotes.toscrape.com](http://quotes.toscrape.com), using [`requests`](https://requests.readthedocs.io/en/latest/) and [`Beautiful Soup`](https://beautiful-soup-4.readthedocs.io/en/latest/). This page is provided by [`Scrapinghub`](https://www.zyte.com/) as a more realistic scraping playground. Take some time to explore the page. We’ll scrape out all the information, that is:

* The quotes, with their author and tags
* And the author information, that is, date and place of birth, and description.

We’ll store this information in a SQLite database. Instead of using the [`records`](https://github.com/kennethreitz/records) library and writing manual SQL statements, we’re going to use the [`dataset`](https://dataset.readthedocs.io/en/latest/) library. This library provides a simple abstraction layer removing most direct SQL statements without the necessity for a full ORM model, so that we can use a database just like we would with a CSV or JSON file to quickly store some information. Installing [`dataset`](https://dataset.readthedocs.io/en/latest/) can be done easily through pip:

`pip install -U dataset`

> Not a Full ORM
> 
> Note that dataset does not want to replace a full-blown ORM (Object Relational Mapping) library like [SQLAlchemy](https://www.sqlalchemy.org/) (even though it uses [SQLAlchemy](https://www.sqlalchemy.org/) behind the scenes). It’s meant simply to quickly store a bunch of data in a database without having to define a schema or write SQL. For more advanced use cases, it’s a good idea to consider using a true ORM library or to define a database schema by hand and query it manually.
