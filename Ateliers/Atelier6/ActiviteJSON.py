import os
from tinydb import TinyDB, Query, where

os.remove('data1.json')

def create_json_file(fichier):
    db = TinyDB(fichier, indent=4)
    print("Contents of 'data.json before:")
    print(db.all())
    db.insert_multiple([
        {"name":"Bob","score":2},
        {"name":"Nefeli","score":10},
        {"name":"Veroniki","score":0.6}])
    print(db.all())
    #print("C'est la base de donnes\n", db)

def read_json_file(fichier):
    User = Query()
    db = TinyDB(fichier, indent=4)
    patrick_list = db.search(User.name == "Patrick")
    print("patrick_list\n",patrick_list)

    patrick_unique = db.get(User.name == "Patrick")
    print("patrick_unique\n",patrick_unique)

    print("Contents after\n", db.all())

    high_scores = db.search(where("score") > 2)
    print("high_scores\n",high_scores)

def update_json_file(fichier, cle, valeur):
    db = TinyDB(fichier, indent=4)
    db.insert({cle:valeur})
    print("\n ---- La base de donnes apres la modification -----\n", db.all())

    #db.update({"score":10}, where('name')=='Patrick')

    #endiaferouses paremvaseis sth bash dedomenon
    #db.update({"role":["Junior"]})
    #db.update({"role":["Programmeur_Python"]}, where('name')=='Patrick')
    #db.upsert({"name":"Pierre", "score":0, "role":["Senior"]}, where('name') == 'Pierre')

def display_data(fichier):
    db = TinyDB(fichier, indent=4)
    print("\n ---- La base de donnes en fin -----\n", db.all())

nom_fichier = 'data1.json'
create_json_file(nom_fichier)
read_json_file(nom_fichier)
cle = 'kati'
valeur = 8
update_json_file(nom_fichier, cle, valeur)
display_data(nom_fichier)

