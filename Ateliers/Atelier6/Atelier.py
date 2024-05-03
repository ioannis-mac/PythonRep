import os, csv
import pandas as pd
import numpy as np

os.remove("ventes.csv")
fp = open("ventes.csv", "x")

mydata = [
    {'Date':"1996-08-04",'Produit':"cafe",'Quantite':40,"Prix":8},
    {'Date':"1997-08-04",'Produit':"vanilla",'Quantite':4,"Prix":40},
    {'Date':"1998-08-04",'Produit':"feta",'Quantite':5,"Prix":6},
    {'Date':"1996-08-04",'Produit':"raclette",'Quantite':0,"Prix":7},
    {'Date':"2000-08-04",'Produit':"pain",'Quantite':8,"Prix":4},
    {'Date':"1996-08-07",'Produit':"juice",'Quantite':4,"Prix":3},
]
#Create the file and write
with open('ventes.csv','w') as fichier:
    colonnes=['Date', 'Produit', 'Quantite', "Prix"]
    ecrivain = csv.DictWriter(fichier,fieldnames=colonnes)
    ecrivain.writeheader()
    for ligne in mydata:
        ecrivain.writerow(ligne)

#open the file and see content
with open('ventes.csv','r') as fichier:
    lecteur = csv.DictReader(fichier)
    aList = []
    for ligne in lecteur:
        print("Reading:",ligne)
        aList.append(ligne)
    
    df = pd.DataFrame(columns=["Date","Produit", "Quantite", "Prix"],
                  data=aList)
    #print("Le list est:\n", aList)

df_csv_content = pd.read_csv("ventes.csv")
print("df to csv: ", df_csv_content)
print("Affiche tous les ecrits\n",df)


#demande 1
"""
print("Le premieres 5 lignes\n",df.head())

#demande 2
#print("Le sum est:\n", sum(df))
df["chiffre d'affairs"] = df_csv_content["Quantite"] * df_csv_content["Prix"]

print("Le sum est: ", df["chiffre d'affairs"])

#demande 3
aGroup=df_csv_content.groupby('Prix')
print(aGroup)
print("max Prix est: ", aGroup.idxmax().tail(1))

#demande 4
produit_plus_vendu = df_csv_content.groupby('Produit')['Quantite'].sum().idxmax()

print("meilleure chiffre d'affairs\n",produit_plus_vendu)

#demande 5
import matplotlib as plt

ventes = df_csv_content.groupby('Produit')["Chiffre d'affaires"].sum()
ventes.plot(kind='bar')
plt.title("Title")
plt.xlabel('Label x')
plt.ylabel('Label y')
plt.show()

"""

