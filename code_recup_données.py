from bs4 import BeautifulSoup
import requests
import os
import csv
import pandas as pd

os.chdir("E:/SAE_BDD")

text_html=requests.get("https://fr.wikipedia.org/wiki/Liste_des_%C3%A9pisodes_de_Gotham").text
soup=BeautifulSoup(text_html,"lxml")
names=soup.find_all('div',class_="mw-content-ltr mw-parser-output")
# Recupération de la liste des episodes
for title in names:
    saison_en_cours = None
    for element in title.find_all('h3'):
        saison_en_cours = element.text.strip()
    noms_des_episodes_saison = []
    for nom in title.find_all('li'):
        if  saison_en_cours:# Si on est dans une saison
            noms_des_episodes_saison.append(nom.i.text)

#Nettoyage des données
for i in range(3):
      noms_des_episodes_saison.remove("Gotham")

# Separer les Episode par saison
Episodes_saison1 =noms_des_episodes_saison[noms_des_episodes_saison.index('Bruce Wayne'):noms_des_episodes_saison.index('Gotham à feu et à sang') + 1]

Episodes_saison2 = noms_des_episodes_saison[noms_des_episodes_saison.index('Le Secret de Thomas Wayne'):noms_des_episodes_saison.index('Métamorphoses') + 1]

Episodes_saison3 = noms_des_episodes_saison[noms_des_episodes_saison.index('Paradis perdu'):noms_des_episodes_saison.index('Le Chevalier des ténèbres') + 1]

Episodes_saison4 = noms_des_episodes_saison[noms_des_episodes_saison.index('Pax Pingouina'):noms_des_episodes_saison.index('De cendres et de flammes') + 1]

Episodes_saison5 = noms_des_episodes_saison[noms_des_episodes_saison.index("L'Année zéro"):]


df1=pd.DataFrame(Episodes_saison1,columns="Episodes_saison1")

df2=pd.DataFrame(Episodes_saison2,columns=["Nom_des_episodes_s2"])


df3=pd.DataFrame(Episodes_saison3,columns=["Nom_des_episodes_s3"])

df4=pd.DataFrame(Episodes_saison4,columns=["Nom_des_episodes_s4"])

df5=pd.DataFrame(Episodes_saison5,columns=["Nom_des_episodes_s5"])
df = pd.concat([df1, df2, df3, df4, df5],axis=1 ,ignore_index=True)
# Appliquer dropna uniquement sur les colonnes sélectionnées
new_column_names = ['Nom_des_episodes_s1', 'Nom_des_episodes_s2', 'Nom_des_episodes_s3', 'Nom_des_episodes_s4', 'Nom_des_episodes_s5']
df.columns=new_column_names
df.to_csv("Noms_episodes.csv",index=False)





#Recuperation des résumés d'episode
ma_connection= psycopg2.connect(database = "2024_SAE_UFARTE",
                        user = "admindbetu",
                        host= '10.11.159.10',
                        password = "admindebetu",
                        port = "5432")


def recup_resume_episode(nom_csv, saison_num):
    Resume_des_episodes = []

    # Construire l'URL en fonction du numéro de la saison
    url = f"https://www.programme-tv.net/programme/series-tv/r276200-gotham/saisons/{saison_num}/"

    # Récupérer la page HTML
    text_html = requests.get(url).text
    soup = BeautifulSoup(text_html, "lxml")

    # Trouver tous les résumés d'épisodes
    resume = soup.find_all('span', class_="programCollectionSeason-episodesListItemSynopsisText programCollectionSeason-episodesText")

    for texte in resume:
        Resume_des_episodes.append(texte.text)

    # Nettoyage des données
    Resume_des_episodes = [item.strip() for item in Resume_des_episodes]

    # Créer un DataFrame
    df = pd.DataFrame(Resume_des_episodes, columns=[f"resume_ep_saison_{saison_num}"])

    # Sauvegarder les résumés dans un fichier CSV
    df.to_csv(nom_csv, index=False)
    print(f"Les résumés de la saison {saison_num} ont été enregistrés dans {nom_csv}.")

# Exemple d'appel de la fonction pour la saison 1
recup_resume_episode("resume_episodes_s1.csv", 1)

# Exemple d'appel pour la saison 2
recup_resume_episode("resume_episodes_s2.csv", 2)

recup_resume_episode("resume_episodes_s3.csv", 3)

recup_resume_episode("resume_episodes_s4.csv", 4)

recup_resume_episode("resume_episodes_s5.csv", 5)






