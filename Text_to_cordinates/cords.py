import json as js
import requests
from bs4 import BeautifulSoup


#TODO Udělání funkce na automatické opravy použitím odkazu -- https://mapy.cz/suggest?q={query} query nahradím adresou inputu a pomoci web scrapingu dostanu cilovou adresu

def suggest(soubor_text):
    pass

    
def place(soubor): 
    with open(soubor, mode="r",encoding="utf-8") as poloha:
        adresa = poloha.read()
        adresa = js.loads(adresa)
        return adresa["place"]

def kordinace(finalni_adresa):
    try:
        zadost = requests.get(f"https://api.mapy.cz/geocode?query={finalni_adresa}")
        parser = BeautifulSoup(zadost.text, "html.parser")
        final = parser.find_all("item")
        return(final[0].get("y") +"   "+final[0].get("x"))
    except IndexError:
        pass


print(kordinace(place("DialCall/Text_to_cordinates/poloha.txt")))
