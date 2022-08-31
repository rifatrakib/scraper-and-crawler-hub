import re
import requests
from bs4 import BeautifulSoup


def get_repo_list(username, is_normal_user=True):
    session = requests.Session()
    
    if is_normal_user:
        url = "https://github.com/{}"
        r = session.get(url.format(username), params={"page": 1, "tab": "repositories"})
        html_soup = BeautifulSoup(r.text, "html.parser")
        repos_element = html_soup.find(id="user-repositories-list")
    else:
        url = "https://github.com/orgs/{}/repositories"
        r = session.get(url.format(username))
        html_soup = BeautifulSoup(r.text, "html.parser")
        repos_element = html_soup.find(class_="repo-list")
    
    return repos_element.find_all("li")


repos = get_repo_list("google", is_normal_user=False)

for repo in repos:
    name = repo.find("h3").find("a").get_text(strip=True)
    language = repo.find(attrs={"itemprop": "programmingLanguage"})
    language = language.get_text(strip=True) if language else "unknown"
    stars = repo.find("a", attrs={"href": re.compile("\/stargazers")})
    stars = int(stars.get_text(strip=True).replace(",", "")) if stars else 0
    print(f"{name=}\t{language=}\t{stars=}")
