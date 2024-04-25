#Practically all=AND, any=XOR

liste1=[True,True,True]
resultat1=all(liste1)
print(resultat1)

liste2=[True,False,True]
resultat2=all(liste2)
print(resultat2)

liste3=[False,False,True]
resultat3=any(liste3)
print(resultat3)

liste4=[False,False,False]
resultat4=any(liste4)
print(resultat4)