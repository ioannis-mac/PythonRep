#act3
"""
def remplissage():
    return {"", donnees1, "age, taille":donnees2}
def consultation():
    return donnees
"""

#act5
"""
def inversion_mots(aListOfWords):
    aList=[]
    for aWord in aListOfWords:
        aString=''
        for i in range(len(aWord)-1,-1,-1):
            aString+=aWord[i]
        aList.append(aString)
    return aList

def mot_palindrome(aListOfWords):
    aListInversed=inversion_mots(aListOfWords)
    aList=[]
    for i in range(len(aListOfWords)):
        if aListOfWords[i]==aListInversed[i]:
            aList.append(aListOfWords[i])
    return aList

aListInitial=["nom","non","union","pop"]
print("The initial List is: ", aListInitial)
print("The inversion mots: ", inversion_mots(aListInitial))
print("The palindrome: ", mot_palindrome(aListInitial))
"""
#act6
def calculatrice(nombre1, nombre2, operation):
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }
    # Vérifier si l'opération est valide
    if operation not in operations:
        raise ValueError("Opération non valide")
    # Récupérer la fonction correspondant à l'opération
    fonction_operation = operations[operation]
    # Appeler la fonction avec les deux nombres en entrée
    resultat = fonction_operation(nombre1, nombre2)
    # Renvoyer le résultat
    return resultat

#Test de la fonction calculatrice
try:
    print(calculatrice(5, 3, '+')) # 8
    print(calculatrice(5, 3, '-')) # 2
    print(calculatrice(5, 3, '*')) # 15
    print(calculatrice(6, 2, '/')) # 3.0
    print(calculatrice(5, 3, '^')) # Erreur : Opération non valide
except ValueError as e:
    print(str(e)) # Affiche l'erreur