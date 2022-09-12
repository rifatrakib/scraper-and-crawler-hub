import requests
from bs4 import BeautifulSoup

url = "http://www.iata.org/publications/Pages/code-search.aspx"

session = requests.Session()
# spoof the user agent as a precaution
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
})

# get the search page
r = session.get(url)
html_soup = BeautifulSoup(r.text, "html.parser")
form = html_soup.find(id="searchForm")

# get the form fields
data = {}
for inp in form.find_all(["input", "select"]):
    name = inp.get("name")
    value = inp.get("value")
    if not name:
        continue
    data[name] = value if value else ""

print(data, end='\n\n\n')
