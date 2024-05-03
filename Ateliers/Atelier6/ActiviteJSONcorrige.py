import os
import json

os.remove('data1.json')

def create_json_file(fichier):
    donnees = {}
    with open(fichier, "+x") as fichier:
        json.dump(donnees,fichier,indent=2)

def read_json_file(fichier) -> dict:
    with open(fichier,"r") as json_file:
        json_donnes = json.load(json_file)
        print("Reading.. :", json_donnes)
    return json_donnes

def update_json_file(fichier, cle, valeur):
    Entry={cle:valeur}

    with open(fichier,"w") as json_file:
        json.dump(Entry, json_file, indent=2)
        

def display_data(fichier):
    json_donnes = read_json_file(fichier)
    print("Displaying.. :", json_donnes)


donnees = {
    "Key" : "It is",
    "Cle" : "Valeur"
}

nom_fichier = "data1.json"
cle = "Haha"
valuer = "Pourquoi tu ris"
create_json_file(nom_fichier)
update_json_file(nom_fichier, cle, valuer)
display_data(nom_fichier)
