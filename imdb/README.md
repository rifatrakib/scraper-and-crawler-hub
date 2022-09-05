## IMDB scraper

This examples moves on toward including some more data science-oriented use cases. We're going to start simple by scraping a list of reviews for episodes of a TV series, using [`IMDB (the Internet Movie Database)`](https://www.imdb.com/). We'll use Game of Thrones as an example, the episode list for which can be found at [http://www.imdb.com/title/tt0944947/episodes](http://www.imdb.com/title/tt0944947/episodes). Note that IMDB's overview is spread out across multiple pages (per season or per year), so we iterate over the seasons we want to retrieve using an extra loop.
