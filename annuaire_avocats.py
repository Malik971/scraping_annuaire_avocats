import re

import requests
from bs4 import BeautifulSoup


def get_all_pages():
    urls = []
    page_number = 1

    for i in range(104):
        i = f"https://www.barreaudenice.com/annuaire/avocats/?fwp_paged={page_number}"
        page_number += 1
        urls.append(i)
    return urls


def parce_attorney(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    attorney = soup.find_all("div", class_="callout secondary annuaire-single")

    for avocat in attorney:
        try:
            nom_avocat = avocat.find("h3", class_="nom-prenom").text.strip()
        except AttributeError as e:
            nom_avocat = ""
        try:
            avocat_adress = avocat.find("span", class_="adresse").text.strip()
        except AttributeError as e:
            avocat_adress = ""
        try:
            ligne_ad = re.sub(r"\s+", " ", avocat_adress)
        except AttributeError as e:
            ligne_ad = ""
        try:
            tel = avocat.find("span", class_="telephone").text.strip()
        except AttributeError as e:
            tel = ""
        try:
            email = avocat.find("span", class_="email").a.text.strip()
        except AttributeError as e:
            email = ""

        chemin = r"C:\Users\Malik\PycharmProjects\scraping_annuaire_avocats\annuaire_avocat.txt"

        with open(chemin, "a") as f:
            f.write(f"{nom_avocat}\n")
            f.write(f"{ligne_ad}\n")
            f.write(f"{tel}\n")
            f.write(f"{email}\n \n")


def parce_all_attorney():
    pages = get_all_pages()
    for page in pages:
        parce_attorney(url=page)
        print(f"On est à la page {page}")


parce_all_attorney()