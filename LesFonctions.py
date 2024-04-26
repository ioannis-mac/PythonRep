def modifier_non_mutable(a,b):
    a = 2 * a
    b = 3 *  b
    print(a,b)

#appel
x=10
y=15
modifier_non_mutable(x,y)
print(x,y)

#ecriture

def modifier_mutable(a,b):
    a.append(8)
    a.append(b) #on peut append une autre matrice aussi
    b[0] = 6
    print("Interieur de la mutable")
    print(a,b)
    print("Finit de modifier")

#appel
lx = [10]
ly = [15]
modifier_mutable(lx,ly)
print("C'est la derniere print")
print(lx,ly)
