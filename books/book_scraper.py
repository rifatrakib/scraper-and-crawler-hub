import re
import dataset
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

db = dataset.connect("sqlite:///books/books.db")
base_url = "http://books.toscrape.com/"


def scrape_books(html_soup, url):
    for book in html_soup.select("article.product_pod"):
        # for now, we'll only store the books url
        book_url = book.find("h3").find("a").get("href")
        book_url = urljoin(url, book_url)
        path = urlparse(book_url).path
        book_id = path.split("/")[2]
        
        # upsert tries to update first and then insert instead
        db["books"].upsert({"book_id": book_id, "last_seen": datetime.now()}, ["book_id"])


def scrape_book(html_soup, book_id):
    main = html_soup.find(class_="product_main")
    
    book = {}
    book["book_id"] = book_id
    book["title"] = main.find("h1").get_text(strip=True)
    book["price"] = main.find(class_="price_color").get_text(strip=True)
    book["stock"] = main.find(class_="availability").get_text(strip=True)
    book["rating"] = " ".join(main.find(class_="star-rating") \
        .get("class")).replace("star-rating", "").strip()
    book["image"] = html_soup.find(class_="thumbnail").find("img").get("src")
    
    desc = html_soup.find(id="product_description")
    if desc:
        book["description"] = desc.find_next_sibling("p").get_text(strip=True)
    
    for row in html_soup.find(string="Product Information").find_next("table").find_all("tr"):
        header = row.find("th").get_text(strip=True)
        # since we'll use the header as a column, clean it a bit
        # to make sure SQLite will accept it
        header = re.sub("[^a-zA-Z]+", "_", header)
        value = row.find("td").get_text(strip=True)
        book[header] = value
    
    db["book_info"].upsert(book, ["book_id"])


# scrape the pages in the catalogue
url = base_url
fresh_start = input("Do you wish to re-scrape the catalogue (y/n)? ")

while fresh_start == "y":
    print(f"Now scraping page: {url}")
    r = requests.get(url)
    html_soup = BeautifulSoup(r.text, "html.parser")
    scrape_books(html_soup, url)
    
    # is there a next page?
    next_page = html_soup.select("li.next > a")
    if not next_page or not next_page[0].get("href"):
        break
    
    url = urljoin(url, next_page[0].get("href"))

# now scrape book by book, oldest first
books = db["books"].find(order_by=["last_seen"])
for book in books:
    book_id = book["book_id"]
    book_url = f"{base_url}catalogue/{book_id}"
    print(f"Now scraping page: {book_url}")
    
    r = requests.get(book_url)
    r.encoding = "utf-8"
    html_soup = BeautifulSoup(r.text, "html.parser")
    scrape_book(html_soup, book_id)
    
    # update the last seen timestamp
    db["books"].upsert({"book_id": book_id, "last_seen": datetime.now()}, ["book_id"])
