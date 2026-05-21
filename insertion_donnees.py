import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import os
os.chdir("D:/SAE_BDD/")
# Charger le fichier CSV
df = pd.read_csv('resume_episodes_s1.csv', encoding="utf-8")  # Ajustez l'encodage si nécessaire

# Connexion à PostgreSQL
db_params = {
    "dbname": "votre_base",
    "user": "votre_utilisateur",
    "password": "votre_mot_de_passe",
    "host": "localhost",
    "port": "5432"
}

try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Création de la table si elle n'existe pas
    create_table_query = """
    CREATE TABLE IF NOT EXISTS episode (
        id SERIAL PRIMARY KEY,
        nom_des_episodes TEXT,
        num_saison INT,
        resume_ep_saison_5 TEXT
    );
    """
    cursor.execute(create_table_query)
    conn.commit()

    # Insérer les données dans la table
    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO episode (nom_des_episodes, num_saison, resume_ep_saison_5) VALUES (%s, %s, %s)",
            (row["nom_des_episodes"], row["num_saison"], row["resume_ep_saison_5"])
        )

    conn.commit()
    print("Données insérées avec succès !")

except Exception as e:
    print("Erreur :", e)

finally:
    cursor.close()
    conn.close()
