import numpy as np
 
# Génération d'un tableau de 100 nombres aléatoires entiers entre 1 et 100
donnees = np.random.randint(1, 101, 100)
 
# Calcul de la moyenne des valeurs du tableau
moyenne = np.mean(donnees)
print("Moyenne :", moyenne)
 
# Calcul de la médiane des valeurs du tableau
median = np.median(donnees)
print("Médiane :", median)
 
# Calcul de l'écart-type des valeurs du tableau
ecart_type = np.std(donnees)
print("Écart-type :", ecart_type)
 
# Sélection des valeurs paires du tableau
donnees_pairs = donnees[donnees % 2 == 0]
print("Données paires :", donnees_pairs)
 
# Sélection des valeurs impaires du tableau
donnees_impaires = donnees[donnees % 2 != 0]
print("Données impaires :", donnees_impaires)
 
# Recherche de la valeur maximale et de son indice dans le tableau
max_value = np.max(donnees)
max_index = np.argmax(donnees)
print("Valeur maximale :", max_value, "à la position (indice) :", max_index)
 
# Tri du tableau par ordre croissant
donnees_triees = np.sort(donnees)
print("Données triées par ordre croissant :", donnees_triees)