from bs4 import BeautifulSoup
import requests
import os
import csv
import pandas as pd


os.chdir("D:/BUT2/SAE3.02")

text_html=requests.get("https://gotham.fandom.com/fr/wiki/Principaux").text
soup=BeautifulSoup(text_html,"lxml")
names=soup.find_all('ul',class_="gallery mw-gallery-packed")
noms_des_episodes_saison1=[]
for name in names:

    for li in name.find_all('li'):
        print(li.text)

    noms=name.find_all('li')



noms_acteurs_principaux=[]
noms_personnages_principaux=[]
for li in noms:
    nom_complet= li.text
    nom_acteur,nom_personnage=nom_complet.strip().split(':')[0],nom_complet.split(':')[-1]
    noms_acteurs_principaux.append(nom_acteur.strip().replace('\xa0', ' '))
    noms_personnages_principaux.append(nom_personnage)
noms_acteurs_principaux = [nom.replace('\xa0', ' ').strip() for nom in noms_acteurs_principaux]
noms_personnages_principaux=[nom.replace('\xa0', ' ').strip() for nom in noms_personnages_principaux]
print(noms_personnages_principaux)
data={"Nom_acteur":noms_acteurs_principaux,"Nom_personnage":noms_personnages_principaux}
Donnees=pd.DataFrame(data)
Donnees.to_csv("data.csv", index=False)


liste_des_noms = []
liste_des_roles=[]

liste_sans_sauts = []

for element in noms_des_episodes_saison1:

    liste_sans_sauts.append(element.strip())

    personnage = element.split(" (")[0]
    liste_des_noms.append(personnage)
for nom in liste_des_noms:
    print(nom)
liste_sans_vides = list(filter(None,liste_des_noms))
for element in liste_sans_sauts:
    role= element.split(" (")[-1]
    liste_des_roles.append(role)
liste_des_roles = list(filter(None,liste_des_roles))
liste_des_roles=[item.replace(')','')for item in liste_des_roles]



print(liste_des_roles)
donnees_csv = [[item] for item in liste_sans_vides]
donnees_role = [[item] for item in liste_des_roles]
tableau=[donnees_csv,donnees_role]
nom_fichier="donnees.csv"
en_tetes=["Nom_des_saison"]
with open(nom_fichier, mode='w', newline='', encoding='utf-8',) as fichier_csv:
    writer = csv.writer(fichier_csv)

    # Écrire les en-têtes
    writer.writerow(en_tetes)

    # Écrire les données
    writer.writerows(donnees_csv)

