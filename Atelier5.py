import numpy as np

donnees = np.random.randint(1,100, 100)

print("donnees: \n", donnees)

print("mean: \n", donnees.mean())

donnees.sort() # il utilise la meme list pour faire le sort

print(donnees.shape)
print(donnees.ndim)
print("mediane: \n", donnees[50])

