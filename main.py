import requests
import csv
from bs4 import BeautifulSoup

#url = "http://annuairesante.ameli.fr/"
url2 = "http://annuairesante.ameli.fr/professionnels-de-sante/recherche.html"

#page = requests.get(url2)

#donnees = {"ps_profession_label": "Médecin généraliste","localisation":"HERAULT (34)"}
payload = {"type": "ps", "ps_profession": "34", "ps_profession_label": "Médecin généraliste", "ps_localisation": "HERAULT (34)",
           "localisation_category": "departements"}

#payload = {"type": "ps", "ps_profession": "34", "ps_profession_label": "Médecin généraliste", "ps_localisation": "HERAULT (34)",
#            "ps_proximite":"on","localisation_category": "departements", "submit_final": "Rechercher",
#            "es_type": "3","ps_sexe": "2", "ps_carte_vitale":"2", "ps_type_honoraire": "indifferent"}

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

#response = requests.post(url, data=donnees)

req = requests.Session()

page = req.post(url2, params=payload, headers=header)

#nom_asc = soup.find_all("option[value='nom_asc']")
#num_asc =
#adresse_asc = soup.find_all("option[value='adresse_asc']")

affichage_result_all = 1

if page.status_code == 200:
    print("formulaire pass")
    donneestoJson = page.json()

    with open("data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["nom_asc", "num-asc", "adresse_asc"])
        writer.writerow([donneestoJson["nom_asc"], donneestoJson["num_asc"], donneestoJson["adresse_asc"]])
else:
    print("error")


soup = BeautifulSoup(page.text, "html.parser")
if affichage_result_all == 1:
    print(soup)



