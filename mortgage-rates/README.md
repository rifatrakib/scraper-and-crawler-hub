## Mortgage Rate Scraper

We're going to scrape Barclays' mortgage simulator available at [https://www.barclays.co.uk/mortgages/mortgage-calculator/](https://www.barclays.co.uk/mortgages/mortgage-calculator/). There isn't a particular reason why we pick this financial services provider, other than the fact that it applies some interesting techniques that serve as a nice illustration.

Take some time to explore the site a bit (using `What would it cost?`). We're asked to fill in a few parameters, after which we get an overview of possible products that we'd like to scrape out.

If you follow along with your browser's developer tools, you'll note that a `POST`  request is being made to [https://www.barclays.co.uk/dss/service/co.uk/mortgages/costcalculator/productservice](https://www.barclays.co.uk/dss/service/co.uk/mortgages/costcalculator/productservice), with an interesting property: the JavaScript on the page performing the POST is using an `application/json` value for the `Content-Type` header and is including the POST data as plain JSON. Depending on requests' data argument will not work in this case as it will encode the POST data. Instead, we need to use the json argument, which will basically instruct [`requests`](https://requests.readthedocs.io/en/latest/) to format the POST data as JSON.

Additionally, you'll note that the result page is formatted as a relatively complex-looking table (with `Show more` links for every entry), though the response returned by the POST request looks like a nicely formatted JSON object; so we might not even need [`Beautiful Soup`](https://beautiful-soup-4.readthedocs.io/en/latest/) here to access this `internal API`.
