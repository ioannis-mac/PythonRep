#act1
"""
x=[]
try:
    n1=int(input("Donner le 1er nombre: "))
    n2=int(input("Donner le 2eme nombre: "))
    x=n1/n2
except ValueError:
    print("Value Error")
    n1=input("Donner le 1er nombre: ")
    n2=input("Donner le 2eme nombre: ")
    x=n1/n2
except ZeroDivisionError:
    print("Division by zero")
    n2=int(input("Donner le 2eme nombre: "))
    x=n1/n2
except :
    print("Something went wrong")
finally:
    print(x)
"""

#act1
"""
with open("input.txt", "r") as myfile:
#myfile=open("input.txt")
    aList=myfile.read()
    aListofNumbers = [eval(i) for i in aList.split(",")]
    #1st print
    print("list is: ",aListofNumbers)
    aSum=sum(aListofNumbers)
    myfile.close()
    for index, elem in enumerate(aListofNumbers):
        #2nd print
        print("index is:", index)
        aListofNumbers[index]-= 5
        aListofNumbers[index] *= aListofNumbers[index]
    #3rd print
    print("list is:", aListofNumbers)

aNewFile = open("output.txt", "x", newline='')
aNewFile.write(str(aListofNumbers))
"""

#act2
"""
while True:
    nom_fichier=input(("Entrez le nom du fichier texte: "))
    try: 
        with open(nom_fichier,"r") as fichier:
            lignes=fichier.readlines()
            nb_lignes=len(lignes)
            print("Le fichier content: ", nb_lignes, "lignes")
        break
    except FileNotFoundError:
        print("Le fichier specifie n'a pas ete trouve. Veuillez verifier le nom du fichier")
    except Exception as e:
        print("Une erreur est survenue lors de la lecture du fichier")
"""

#---- Les procedures et fonctions ----
#act1
"""
somme_pairs='1,-5,7,1045,5,-6,86,75'
aList=[]
aListofNumbers = [eval(i) for i in somme_pairs.split(",")]
for aNumber in aListofNumbers:
    if aNumber%2 == 0:
        aList.append(aNumber)

print(sum(aList))
"""

#act2
"""
def calculer_aire_rectangle(longeur, largeur):
    return longeur*largeur
def calculer_perimetre_rectangle(longeur, largeur):
    return 2*(longeur+largeur)

print(calculer_aire_rectangle(2,3))
print(calculer_aire_rectangle(0,3))

print(calculer_perimetre_rectangle(7,8))
print(calculer_perimetre_rectangle(1,37))
"""

#act3
"""
donnees=[]
def remplissage(diction1):
    #quelque code
    donnees1=str(input("Ecrire un nom SVP: "))
    donnees2=str(input("Ecrire l'age et le taille SVP: "))
    data={'Nom':donnees1, 'age,taille':donnees2}
    donnees.append(data)

def consultation(diction2):
    #quelque code
    return print(diction2)

remplissage(donnees)
consultation(donnees)
"""

#act4
"""
def mediane(aListofNumbers):
    return sum(aListofNumbers)/len(aListofNumbers)

aList=[1,2,3,4,5,6]
print(mediane(aList))
aList2=[1,2,3,4,5,6,7]
print(mediane(aList2))
"""

#act5
def inversion_mots(aListofWords):
    aList=[]
    for aWord in aListofWords:
        aWord.reverse()
        aList.append(aWord)

aList1=["Hello"]
inversion_mots(aList1)

