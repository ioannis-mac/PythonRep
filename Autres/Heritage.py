from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Personne:
    num: str
    nom: str
    prenom: str

    @abstractmethod
    def affichage(self):
        print(self.nom + " " + self.prenom)
        pass


class Etudiant(Personne):
    def __init__(self, num: int = 0, nom: str = '', prenom: str = '', programme: str = '' ):
        super().__init__(num, nom, prenom)
        self.__programme = programme
#    def desole(self):
#        print("Class Etudiant est desole")

class Enseignant(Personne):
    def __init__(self, num: int = 0, nom: str = '', prenom: str = '', salaire: int = 0, programme: str = ''):
        super().__init__(num, nom, prenom)
        self.__salaire = salaire
#    def desole(self):
#        super().desole()

class Doctorant(Enseignant,Etudiant):
    def __init__(self, num: int = 0, nom: str = '', prenom: str = '', salaire: int = 0, programme: str = '', annee: str = ''):
        Enseignant.__init__(self,num, nom, prenom,salaire)
        Etudiant.__init__(self,num, nom, prenom,salaire)
        self.__annee = annee

    @property
    def annee(self) -> str:
        return self.__annee
    
    @annee.setter
    def annee(self, annee: str) -> None:
        self.__annee = annee

    def __str__(self) -> str:
        return super().__str__() + " " + self.__programme + " " + str(self.salaire) + " " + self.get_annee()


p1 = Personne(num=20, nom="Attention a les chaises,", prenom="Amath")

print(p1)

etudiant= Etudiant(123, 'Dupont', 'Jean', 'Inforatique')

print("Apres l'utilization de method abstract")
p1.affichage()