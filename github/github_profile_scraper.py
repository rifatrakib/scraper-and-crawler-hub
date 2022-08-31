import requests
from dotenv import dotenv_values
from bs4 import BeautifulSoup

config = dotenv_values()


session = requests.Session()
url = "https://github.com/{}"
username = "Macuyiko"

r = session.get(url.format("login"))
html_soup = BeautifulSoup(r.text, "html.parser")

data = {}
for form in html_soup.find_all("form"):
    for inp in form.select("input[type=hidden]"):
        data[inp.get("name")] = inp.get("value")

data.update({"login": config.get("GITHUB_USERNAME"), "password": config.get("GITHUB_PASSWORD")})
print("Going to login with the following POST data:")
print(data)

if input("Do you want to login (y/n)? ") == "y":
    r = session.post(url.format("session"), data=data)
    r = session.get(url.format(username))
    html_soup = BeautifulSoup(r.text, "html.parser")
    user_info = html_soup.find(class_="vcard-details")
    print(user_info.text)
