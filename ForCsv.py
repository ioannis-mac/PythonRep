import csv

#create a dictionary
donnees = [
    {'Nom':'Alice', 'Age':25,'Ville':'Paris'},
    {'Nom':'Bob', 'Age':30,'Ville':'Londres'},
    {'Nom':'Charlie', 'Age':22,'Ville':'New York'},
]

#Create the file and write
with open('fichier2.csv','w', newline='') as fichier:
    colonnes=['Nom', 'Age', 'Ville']
    ecrivain = csv.DictWriter(fichier,fieldnames=colonnes)
    ecrivain.writeheader()
    for ligne in donnees:
        ecrivain.writerow(ligne)

#open the file and see content
with open('fichier2.csv','r') as fichier:
    lecteur = csv.DictReader(fichier)
    for ligne in lecteur:
        print(ligne['Nom'], ligne['Age'], ligne['Ville'])