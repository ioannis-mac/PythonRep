#act1
"""
class Rectangle:
    def __init__(self, longeur, largeur):
        self.longeur = longeur
        self.largeur = largeur
    
    def calculer_perimetre(self):
        return self.longeur * 2 + self.largeur * 2
    
    def calculer_aire(self):
        return self.longeur * self.largeur

    def est_carre(self):
        if self.longeur == self.largeur:
            return True
        else:
            return False

r1 = Rectangle(2,3)
r2 = Rectangle(9,9)
print(r1.calculer_perimetre())
print(r1.calculer_aire())
print(r2.est_carre())
"""

#act2
"""
class Point:
    x: int
    y: int
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def deplace(self, dx:int, dy:int):
        self.x += dx
        self.y += dy
        return Point(self.x, self.y)

    def __repr__(self) -> int:
        return f"Point(x={self.x}, y={self.y})"

p1 = Point(1,1)
p2 = Point(3,4)

print("--",p1)
print(p1.deplace(2,4))
"""

#act3
"""
class Bibliotheque():
    def __init__(self, livres: list):
        self.livres = livres 

    def __repr__(self):
        return f"Bibliotheque avec livres: \n {self.livres}"
    
    def ajouter(self, livre: str) -> list:
        return self.livres.append(livre) 

    def retirer(self, livre: str) -> list:
        self.livres.remove(livre)
        return self.livres
    
    def retourner(self, livre: str) -> list:
        return self.ajouter(livre)


class Membre():
    def __init__(self, nom: str, numero: int, livres_empruntes: list):
        self.nom = nom 
        self.numero = numero
        self.livres_empruntes = livres_empruntes

    def __repr__(self):
        return f"Membre(nom={self.nom}, numero={self.numero}, livres={self.livres_empruntes})"
        
    def emprunter(self, livre: str) -> list:
        return self.livres_empruntes.append(livre)

class Livre():
    def __init__(self, titre: str, Auteur: str, annee: int, ISBN: int):
        self.titre = titre
        self.Auteur = Auteur
        self.annee = annee
        self.ISBN = ISBN
    
    def __repr__(self):
        return f"Livre(titre={self.titre}, Auteur={self.Auteur}, annee={self.annee}, ISBN={self.ISBN})"
    
# On teste ici
print("------------- Les donnees ---------------")
m1 = Membre('ioannis', 1, ["livre1", "livre2"])
print(m1)
l1 = Livre('La peste', "Albert Camy", 1925, 123456789)
print(l1)
b1 = Bibliotheque(["livre10", "livre25"])
print(b1)

# Ajouter un livre
print("\n------------- AJOUTER ---------------")
b1.ajouter(l1.titre)
print(b1)

#Retirer un livre
print("\n------------- RETIRER ---------------")
b1.retirer(b1.livres[1])
print(b1)

#Emprunter un livre
print("\n------------- EMPRUNTER---------------")
m1.emprunter("La peste")
print(m1)

# Retourner un livre
print("\n------------- RETOURNER ---------------")
b1.retourner(m1.livres_empruntes[0])
print(b1)
print(m1)
"""
#act4
"""
class CompteBancaire:
    def __init__(self, titulaire: str, solde = 0) -> None:
        self.titulaire = titulaire
        self.__solde = solde
        #il faut utilise le prive

    def deposer(self, montant: int) -> int:
        self.__solde += montant
        return self.__solde

    def retirer(self, montant: int) -> int:
        depot = self.__solde - montant
        if depot > 0:
            print(f"Depot accepte. Votre depot est mis a jour. C'est: {depot}.0 EUR")
            self.__solde = depot
            return self.__solde 
        else:
            print(f"Votre depot n'est pas suffit pour retirer le montant de: {montant}.0 EUR. Essayez avec une autre montant SVP.\n")

    def consultation_solde(self) -> int:
        return self.__solde
    
    def __str__(self):
        return f"Compte(nom={self.titulaire}, montant={self.__solde}.0 EUR.)"
        
compte1 = CompteBancaire("Amath")

# Deposer
compte1.deposer(1000000)
print(compte1)

# Retirer
compte1.retirer(1)
compte1.retirer(1000001)
print(compte1)

# Consultation
compte1.consultation_solde()
print(compte1)
"""

#act6

class Employe:
    nombre_employes = 0
    pourcentage = 0
    
    # Nombre de les employes
    @staticmethod
    def increment() -> None:
        Employe.nombre_employes += 1

    # Augmentation de salaire
    @staticmethod
    def augmentation_salaire(N):
        Employe.augmentation = N

    def __init__(self, nom: str = '', salaire: int = 0):
        self.__nom = nom
        self.__salaire = salaire

    def afficher_informations(self):
        nouveau_sal = self.__salaire + self.__salaire * self.augmentation / 100
        print(f"L'employe ave nom: {self.__nom}, est {nouveau_sal} EUR/mois base de salaire.")

    def __str__(self):
        return f"Employe avec nom: {self.__nom} et salaire: {self.__salaire} EUR/mois."


# Tester
print(Employe.nombre_employes)
emp1 = Employe("ioannis", 10)
print(emp1)
print(Employe.nombre_employes)

# Augemntation de salaire
emp1.augmentation_salaire(5)

# Affichage
emp1.afficher_informations()
#Peut-etre exprimer les objet a la fin? 