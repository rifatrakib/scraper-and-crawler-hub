import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "http://www.iata.org/publications/Pages/code-search.aspx"


def get_airlines_data(airlines_name):
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
        if "ddlImLookingFor" in name:
            value = "ByAirlineName"
        if "txtSearchCriteria" in name:
            value = airlines_name
        
        data[name] = value if value else ""
    
    r = session.post(url, data=data)
    html_soup = BeautifulSoup(r.text, "html.parser")
    table = html_soup.find("table", class_="datatable")
    df = pd.read_html(str(table))
    
    return df


df = get_airlines_data("Lufthansa")
print(df)
