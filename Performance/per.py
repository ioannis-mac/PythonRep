import datetime
import random

start_time = datetime.datetime.now()


#act1

class Personne:
    def __init__(self, nom: str, prenom: str):
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
        return f"Personne(nom={self.nom}, prenom={self.prenom}.)"

    
class Client(Personne):
    def __init__(self, nom :str, prenom: str, numero: int):
        super().__init__(nom,prenom)
        self.__numero = numero

class Reservation():

    aListDeRes = []
    ResNumero = 0

    @staticmethod
    def increment():
        Reservation.ResNumero += 1

    def __init__(self, NombreDePersonnes: int, date: str, heure: str):
        self.__NombreDePersonnes = NombreDePersonnes
        self.__date = date
        self.__heure = heure
        Reservation.increment()
        #print("Une reservation est demande. Le nombre des reservations Demande est: ", Reservation.ResNumero)
    
    def reserver(self, nomRes: str)-> list:
        estDans = False
        for aRes in Reservation.aListDeRes:
            if nomRes == aRes:
                estDans = True
                
        if estDans:
            #print("\nLa table que le client demande est reserve: \nLa list de table reserve est:", Reservation.aListDeRes, "\n")
            print("")
        else:
            Reservation.aListDeRes.append(nomRes)
            #print("\nUne reservation est accepte. La somme de list de res est: ", Reservation.aListDeRes, "\n")


    def __str__(self):
        return f"Reservation(Nombre de personnes={self.__NombreDePersonnes}, Date={self.__date}, Heure={self.__heure}.)"


#act2

class Table:
    def __init__(self, numero: int, capacite: int):
        self.__numero = numero
        self.__capacite = capacite

    def __str__(self):
        return f"numero:{self.__numero}, capacite: {self.__capacite} "
    
class TableRonde(Table):
    def __init__(self, numero: int = 0, capacite: int = 0, cake: bool = True):
        super().__init__(numero, capacite)
        self.__cake = cake

    def __str__(self):
        return super().__str__() + " cake:" + str(self.__cake) + " \n"

class TableCaree(Table):
    def __init__(self, numero: int = 0, capacite: int = 0, cafe: bool = True):
        super().__init__(numero, capacite)
        self.__cafe = cafe

    def __str__(self):
        return super().__str__() + " cafe:" + str(self.__cafe) + " \n"

#act3
class Article():
    def __init__(self, article: str, prix: int):
        self.__article = article
        self.prix = prix

    def __str__(self) -> str:
        return f"article:{self.__article}, prix: {self.prix}"

class CommandeArticle(Article):
    def __init__(self, article: str, prix:int, quantite: int = 1):
        super().__init__(article, prix)
        self.quantite = quantite
    
    def __str__(self) -> str:
        return super().__str__() + ", quantite: " + str(self.quantite) + "\n"

class Commande():
    def __init__(self, client, articles):
        self.__client = client
        self.__articles = articles

    def calculer_total(self): 
        return sum(art.prix * art.quantite for art in self.__articles) # il faut qu ils sont publiques? OUI! 
    
    def __str__(self):
        return f"client:" + str(self.__client) + ", articles:" + str(self.__articles)


#act4
class Ouvrier(Personne):
    def __init__(self, nom, prenom, identifiant, poste):
        super().__init__(nom, prenom)
        self.identifiant = identifiant
        self.poste = poste

class Absence:
    def __init__(self, ouvrier, date, raison ):
        self.ouvrier = ouvrier
        self.date = date
        self.raison = raison

    def afficher_abs(self):
        #print(f"Nom: {self.ouvrier.nom}, prenom: {self.ouvrier.prenom}")
        #print("Identifiant: " + str(self.ouvrier.identifiant) + " Date:" + self.date + ", Raison:" + self.raison + "\n")
        print("")

class Horaire:
    def __init__(self, debut, fin):
        self.debut = debut
        self.fin = fin

    def __str__(self) -> str:
        return f"Horaire: {self.debut} - {self.fin}"

class HoraireFlexible(Horaire):
    def __init__(self, debut, fin, plage):
        super().__init__(debut, fin)
        if plage > 0:
            self.fin += plage
        elif plage < 0:
            self.debut -= plage
        else: 
            self.debut -= plage
            self.fin += plage

    def __str__(self) -> str:
        return super().__str__() 

class Equipe:
    def __init__(self) -> None:
        pass

class ChefEquipe(Ouvrier):
    def __init__(self, ouvrList: list) -> None:
        super().__init__()
        self.ouvrList = ouvrList

    def methode_ajouter(self, ):
        self.ouvrList.append()

class Main:
    def test_reservation(self):
        # TESTER
        #print("---- Bienvenue a la restaurant 'M&D: Manger et apres Dormir' ----- \
            #\n Les nombre des reservations total est: ", Reservation.ResNumero, "\n")

        p1 = Personne("Frere", "Jacques")
        c1 = Client("Veroniki", "Sarri", 1)
        r1 = Reservation(2, "22/03", "12:30")

        # 
        #print(p1)
        #print(c1)
        #print(r1)

        # Esayer de reserver
        r1.reserver("1er table")
        # Re-essayer de faire une reservation avec une table reserve
        r1.reserver("1er table")

        # Faire une deuxieme reservation
        r1.reserver("2eme table")

    def test_table(self):
        # Tester
        tableAbstract = Table(1, 2)

        #print(tableAbstract)

        # Creer une table ronde
        r1 = TableRonde(1,2,False)
        #print(r1)

        # Creer une table carree
        c1 = TableCaree(1,2,True)
        #print(c1)

    def test_article(self):
        # Tester
        commande1 = Commande("ioannis",3)
        #print(commande1)

        # Creer un menu
        art1 = Article("raclette", 1)
        art2 = Article("cafe glace", 3)
        art3 = Article("vin", 7)
        art4 = Article("pates", 50)
        art5 = Article("gateau", 8)
        art6 = Article("pizza", 12)
        #print(art1, art2, art3, art3, art4, art5, art6)

        comPour = CommandeArticle("raclette", 3)

        #print(comPour)
        
    def test_commande(self): 
        client = Client("Dupont", "Jean", 2) 
        article1 = CommandeArticle("Chaise", 50.0, 2) 
        article2 = CommandeArticle("Table", 150.0, 1) 
        article3 = CommandeArticle("Lampe", 20.0, 3) 
        articles = [article1, article2, article3] 
        commande = Commande(client, articles)
        total = commande.calculer_total() 
        #print(f"Le total de la commande est : {total} €")

    def test_absences(self):
        o1 = Ouvrier("ioannis", "nom", 24, "DEV")
        #print(o1)
        a1 = Absence(5, "today", "maladie")
        absences = a1.afficher_abs()
        #print("Les absences sont: ", absences)
    
    def test_horaires(self):
        h1 = Horaire(9,17)
        h2 = HoraireFlexible(h1.debut, h1.fin ,+3)
        #print("L'horaire avant: ", h1)
        #print("L'horaire flexible apres: ", h2)
        h3 = HoraireFlexible(h1.debut, h1.fin ,-1)
        #print("L'horaire flexible apres: ", h3)
        h4 = HoraireFlexible(h1.debut, h1.fin ,1)
        #print("L'horaire flexible apres: ", h4)

    def test_equipes(): 
        ouvrier = Ouvrier("Martin", "Luc", "O123", "Soudeur") 
        absence = Absence(ouvrier, "12-03", "Rendez-vous médical") 
        absence.afficher_abs()

if __name__ == "__main__":
    # Classe principal
    main = Main()
    main.test_reservation()
    main.test_table()
    main.test_article()
    main.test_commande()
#    main.test_absences()
#    main.test_horaires()
#    main.test_equipes()

start_time1 = datetime.datetime.now()
random_elements = random.sample(range(0,10000000), 1000)
list_seq = list(range(1000000)) #list

counter = 0
for elem in random_elements:
    if elem in list_seq:
        counter +=1


end_time=datetime.datetime.now()

print("Le difference 1: " +  str((end_time - start_time1).microseconds) + " microSec")
print("Le difference 1: " +  str((end_time - start_time1).seconds) + " Sec")

start_time2 = datetime.datetime.now()
random_elements = random.sample(range(0,10000000), 1000)
list_seq = set(range(1000000))

counter = 0
for elem in random_elements:
    if elem in list_seq:
        counter +=1


end_time2=datetime.datetime.now()

print("Le difference 2: " +  str((end_time2 - start_time2).microseconds) + " microSec")
print("Le difference 2: " +  str(end_time2 - start_time2)+ " Sec")