import requests
from bs4 import BeautifulSoup


# fonction
def scape_title(url):
    r = requests.get(url)
    bs = BeautifulSoup(r.content, "html.parser")
    titre = bs.h1
    return titre


title = scape_title("https://scrap.io/fr?city=Montpellier&country=FR&type=restaurant")
print(title)