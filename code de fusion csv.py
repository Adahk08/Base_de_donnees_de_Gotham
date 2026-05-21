import pandas as pd
import glob

import os

os.chdir("C:/Users/user/Documents/SAE_BDD")
chemin="C:/Users/user/Documents/SAE_BDD/*.csv"

tous_les_fichiers=glob.glob(chemin)

data=[]

for fichier in tous_les_fichiers:
    data.append(pd.read_csv(fichier))

All_data=pd.concat(data,ignore_index=True)
All_data.to_csv("Data.csv",index=False)
