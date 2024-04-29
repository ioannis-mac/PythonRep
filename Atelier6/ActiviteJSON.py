import os
from tinydb import TinyDB, Query, where



def create_json_file(fichier):
    db = TinyDB('data1.json', indent=4)
    print("Contents of 'data.json before:")
    print(db.all())
    db.insert_multiple([
        {"name":"Bob","score":2},
        {"name":"Nefeli","score":10},
        {"name":"Veroniki","score":0.6}])
    print(db.all())

print("C'est la base de donnes\n", db)

os.remove('data1.json')


db.insert({"name":"Patrick","score":0})
#print(db.drop_table(db.table))




patrick_list = db.search(User.name == "Patrick")
print("patrick_list\n",patrick_list)

patrick_unique = db.get(User.name == "Patrick")
print("patrick_unique\n",patrick_unique)

print("Contents after\n", db.all())

high_scores = db.search(where("score") > 2)
print("high_scores\n",high_scores)

db.update({"score":10}, where('name')=='Patrick')

#endiaferouses paremvaseis sth bash dedomenon
db.update({"role":["Junior"]})
db.update({"role":["Programmeur_Python"]}, where('name')=='Patrick')
db.upsert({"name":"Pierre", "score":0, "role":["Senior"]}, where('name') == 'Pierre')

#suppression
db.remove(where('score')==0)
#db.truncate() # vider la base de donnees
users = db.table("Users")
roles = db.table("Roles")

#users.insert