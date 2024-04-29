from dataclasses import dataclass

@dataclass
class Person:
    num: str
    nom: str
    prenom: str

person = Person(num=20, nom="Attention a les chaises,", prenom="Amath")

print(person)
