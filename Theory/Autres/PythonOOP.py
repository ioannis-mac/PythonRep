"""
class Personne:
    def __init__(self, num:int, nom:str, prenom:str): # Default constructor
        self.num = num
        self.nom = nom
        self.prenom = prenom

class Personne2:
    def __init__(self, num:int, nom:str, prenom:str): # Default constructor
        self.num = num
        self.nom = nom
        self.prenom = prenom
# The __repr__() representation is intended to hold information about the object so that it may be created again.
# In contrast, the __str__() string representation is human-friendly and mainly used for logging reasons. 
# Always utilize the str() and repr() functions instead of using these methods directly.
    def show_data(self):
        print("Show data funtion was called")
        print("Data: ", self.nom, self.prenom)

    def __str__(self)->str:                         # To print the detailes of the object in a human readable format
        return self.prenom+" "+self.nom
    
    def __repr__(self):                             # to hold info in less human readable format, depending on construction
        return f"Personne(x={self.prenom}, y={self.nom})"

# p = Personne() Ca donne une erreur
p = Personne(1, "g", "b")
p.num = 100
p.prenom = 'Amath'
p.nom = 'Tres bien'
print(p.num, p.prenom, p.nom)

p2 = Personne2(1, 'Eythimiou', 'Veroniki')
p2.show_data()
print("Affiche les detailes par __str__: ", p2)
print("Afiche avec __repr__: ", repr(p2))
"""
class Personne3:
    nb_personnes = 0
    def __init__(self, num:int = 0 , nom:str = '', prenom:str = ''): # Default constructor
        self.__num = num
        self.__nom = nom
        self.__prenom = prenom
    # So technically here we declared them private

    # Number of people
    @staticmethod
    def increment_nb_personnes() -> None:
        Personne3.nb_personnes += 1

    # SETTERS
    def set_num(self, num: int) -> None:
        self.__num = num
    def set_nom(self, nom: int) -> None:
        self.__nom = nom
    def set_prenom(self, prenom: int) -> None:
        self.__prenom = prenom

    #GETTERS
    def get_num(self) -> int:
        return self.__num
    def get_nom(self) -> str:
        return self.__nom
    def get_prenom(self) -> str:
        return self.__prenom
    # ATTENTION to the differences of the syntax

    # For releasing memory
    def del_num(self) -> None:
        del self.__num

    def __del__(self):                              # Default Destructor
        print("Destructor called")
        print(f"Person {self.__nom} is being deleted")

    def __str__(self) -> str:
        return str(self.__num) + " " + self.__prenom + " " + self.__nom

    def append_nom(self, nom:int) -> None:
        self.__nom += nom

    # Publish the private attributes here
    num = property(get_num, set_num)
    nom = property(get_nom, set_nom)
    prenom = property(get_prenom, set_prenom)


# Here are the tests of the FUNCTIONS/METHODS of the class
p = Personne3(101, 'Dubois', 'Pierre')
print("Print with __str__: \n", p)
# here we change/replace the info
p.set_num(202) 
p.set_prenom('Daniel')
#p.append_nom('Beau') # if I want to append info
print("Print after setters: \n", p)
# p.get_prenom('Daniel')
print("Print with getters: \n", p.get_num(), p.get_nom(), p.get_prenom())

p.num = 505
p.prenom = 'John'
print("Print after the publishing of private attributes:\n", p)

# Testing the increment depending if it is static or not
print("Number of people: ", Personne3.nb_personnes) 

# Test the deleter
del p
print(p)