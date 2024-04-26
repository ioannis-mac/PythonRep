#act9

#str(input("Entrer une phrase SVP:"))
"""
texte='Une phrase avec les mots'

ListDeMots=[]
aWord=''
for aChar in texte:
    if aChar != ' ':
        aWord+=aChar
    else:
        ListDeMots.append(aWord)
        aWord=''    

print("List de mots: ", ListDeMots)
nombreDeMots=0
LePluslongue=[]
for aWord in ListDeMots:
    nombreDeMots+=1
    for aChar in aWord:
        LePluslongue[nombreDeMots]+=1

print("Nombre de mots est: ", nombreDeMots)
print("Le plus longue", LePluslongue)
"""

#act10
"""
aList=int(input("Ecrire a list: "))

est_symmetrique = (nombres === nombres[::-1])
"""

#act 4
menu={}
menu['1']='ajouter Etudiant'


options=menu.keys()
for entry in options:
    print(menu[entry])
for entry in options:
    selection=input("Selectrioner SVP: ")
    if selection =='1':
        print("ajout")

