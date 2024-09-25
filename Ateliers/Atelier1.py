#act1
"""
message = 'Hello world'
message = 'Hello world'
New_message = 'Hi there'
print(message.upper)
print(message.lower())
#print(message.count())
nom = input("Veuillez entrer votre nom SVP")
a='c'
b=123
d=a+str(b)
"""

#act2
"""
x=int(input("Entrer un nombre SVP: "))
y=int(input("Entrer le deuxieme nombre SVP: "))
print("C'est la somme", x+y)
"""

#Les structures conditionnels
#act1
"""
x=int(input("Entrer un nombre SVP: "))
y=int(input("Entrer le deuxieme nombre SVP: "))
z=int(input("Entrer le troisieme nombre SVP: "))
print("Max: ",max(x,y,z))
max=-10000000
if x>y and x>z:
    max=x
elif y>x and y>z:
    max=y
else:
    max=z
print("Maxi avec if is: ", max)
"""
#act2
"""
import random
randN=random.randint(1, 100)
x=int(input("Deviner ce nombre: \n"))
dif= x-randN

while dif!=0:
    if dif == 0:
        print("Trouve!")
        break
    elif dif<0:
        print("Trop petit")
    else:
        print("trop grandi")
    x=int(input("Deviner ce nombre: \n"))
    dif= x-randN
print("Trouve!")
"""

#act3
"""
import string
est_pairs=True
positif=str(input("Saisir un nombre entier positif SVP: "))
for chiffre in positif:
    if (int(chiffre)%2 != 0):
        est_pairs=False
if est_pairs:
    print("Ils sont pairs")
else:
    print("Ils ne sont pas pairs")
"""

#Les boucles
#act1
"""
positif=int(input("Saisir un nombre entier positif SVP: "))

for i in range(positif):
    print(i, ", ")
print(positif)
"""

#act2
"""
a=0
b=10

print("Boucle de a")
while a<b:
    print(a)
    a+=1
print("Boucle de b")
while b>0:
    if b%2 != 0:
        print(b)
    b-=1
"""

#act3
"""
n=int(input("Saisir un nombre SVP: "))
for i in range(n, n+1):
    i*=i
print("Le prod est: ", i)
"""
#act4
"""
chaine=str(input("Ecrivez un chaine SVP: "))
for index, aCharacter in enumerate(chaine ,start=1):
    if aCharacter == 'a':
        print("a est dans la chaine a la position: ", index)
"""

#act5
"""
t='Python est un merveilleux langage de programmation'
for index, aCharacter in enumerate(t ,start=1):
    if aCharacter == ' ':
        break
print(t[0:index])
"""

#act6
"""
texte=str(input("Exrivez un texte SVP: "))
list1=[]
aWordToList=list(texte)
aString=''
for aChar in aWordToList:
    if aChar != ' ':
        aString+=aChar
    else:
        list1.append(aString)
        aString=''

list1.append(aString)

# Si un mot commence pas par le lettre 'b' n'affiches pas
for aWord in list1:
    if (aWord[0] != 'b'):
        list1.remove(aWord)
print(list1)
"""

#act8
"""
mul=int(input("Ecrivez le mul SVP: "))
bornInf=int(input("Ecrivez le bornInf SVP: "))
bornSup=int(input("Ecrivez le bornSup SVP: "))

for i in range(bornInf, bornSup+1):
    somme=i*mul
    print(i," x ", mul, " = ", somme)
"""

#act9
"""
texte=str(input("Exrivez une phrase SVP: "))
#texte='The best in Brazil'
list1=[]
#convert to a list
aWordToList=list(texte)

#Separate the words
aString=''
for aChar in aWordToList:
    if aChar != ' ':
        aString+=aChar
    else:
        list1.append(aString)
        aString=''
list1.append(aString)

#Compter le nombre total de mots de phrase
NombrTotal=0
for aWord in list1:
    NombrTotal+=1
print("Nombre total de mots: ", NombrTotal)
NombreDeChaqueMot=[0]*NombrTotal

#compter le nombre de characteres de chaque mot
i=0
for aWord in list1:
    for aChar in aWord:
        NombreDeChaqueMot[i]+=1
    i+=1
print("Nombre total de chaque mot: ", NombreDeChaqueMot)

#trouver la mot la plus longue
maximumLettres=max(NombreDeChaqueMot)
index=0
for elem in NombreDeChaqueMot:
    if (elem == max(NombreDeChaqueMot)):
        IndexMot=index
    index+=1
print('Le mot le plus longue est: "', list1[IndexMot], '" avec une somme de: ', max(NombreDeChaqueMot))
#Afiche la phrase en inversant l'ordre des mots
list1.reverse()
print("La liste inverse est: ", list1)
list1.reverse()

print("La liste initial est: ", list1)
"""

#act10
#list1=int(input("Tapper un list SVP: "))
"""
list1=[8,-3,15,4,7]

print("Sum of list is: ", sum(list1))
print("Le nombre de plus grand de list est: ", max(list1))
numberOfElem=0
for i in list1:
"""