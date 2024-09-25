#act1
"""
aPositif=int(input("saisir un nombre entier positif SVP: "))
print(*range(1, aPositif+1,2))
#star is for kind of dereferencing the return value?
#Elseway it would print it the inside of print as a string -> output: "range(1, aPositif+1,2)"
#only for iterable arguments
"""

#act2
"""
aChaine=str(input("saisir une chaîne de caractères SVP: "))
print(*[(char, ord(char)) for char in aChaine])
"""
#act3
"""
aChaine=str(input("saisir une chaîne de caractères SVP: "))
print(aChaine[::-1])
"""

#act4
"""
phrase=str(input("saisir une chaîne de caractères SVP: "))
print(*[len(word) for word in phrase.split()])
# syntax     |          |            |
# syntax: return       arg       splits by ' '
"""

#act5
"""
aPositif=int(input("saisir un nombre entier positif SVP: "))
print(sum(range(aPositif)))
"""

#act6
"""
#aChaine=str(input("saisir une chaîne de caractères SVP: "))
aChaine="saisir une chaîne de caractères SVP: "
print(*[word[::-1] for word in aChaine.split()])
"""
#act7
"""
aNombre=int(input("saisir un nombre entier positif SVP: "))
print(*[i for i in range(1, aNombre) if aNombre%i==0] )

#print(*[range(1, aNombre)/i for i in range(1, aNombre) ] )
"""

#act8
"""
aChaine1=str(input("Entrer le premier chaine: "))
aChaine2=str(input("Entrer le deuxieme chaine: "))
print(max(aChaine1, aChaine2, key=len) )
print(aChaine1 if len(aChaine1) > len(aChaine2) else aChaine2)
print(aChaine1 if aChaine1 > aChaine2 else aChaine2)
"""

#act9
"""
aChaine=str(input("Entrer le chaine: "))
voyelles="aeiouAEIOU"
print(''.join(char for char in aChaine if char not in voyelles))
"""

#act10
aNombre=int(input("saisir un nombre entier SVP: "))
print( *[i for i in range(aNombre+1) if all(i%j!=0 for j in range(2,aNombre))]) 
#print( *[i for i in range(aNombre+1) if all(i%x!=0 for x in range(2,int(i**0.5)+1) )]) 