print("bonjour")
a=5
print(a)
print("a vaut ",a)
nom = "Alice"
age=30
print("Bonjour, je m'appelle {} et j'ai {} ans.".format(nom,age))
print(f"Bonjour, je m'appelle {nom} et j'ai {age} ans.")
print('I have %d cats' % 6)
print('I have %3d cats' % 6)
print('I have %03d cats' % 6)
print('I have %f cats' % 6)
print('I have %.2f cats' % 6)

l=[12,7,8,4,9]
for i in l:
    print(i, end='')

prenom=input("Entrez votre prenom:")
print("Bonjour", prenom)

# Ceci est un commentaire

b=float(input("Entrez un donnee numerique:"))
print("Votre donnee numerique est: ", b)

"""
Commentaire en plusiers
lignes 
"""
variable_un='apostrophes'
variable_deux="guillemets"
age="J'ai 26 ans"
age2='J\'ai 26 ans'
print(age+age2)