#act1
import numpy as np
"""
# mon epreuve -------
import numpy as np

donnees = np.random.randint(1,100, 100)

print("donnees: \n", donnees)

print("mean: \n", donnees.mean())

donnees.sort() # il utilise la meme list pour faire le sort

print(donnees.shape)
print(donnees.ndim)
print("mediane: \n", donnees[50])

# mon epreuve --------


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
"""

#act2
"""
notes_maths = np.random.uniform(10,20, size=20)
notes_physiques = np.random.uniform(12,18, size=20)
print(f"notes_maths: \n{notes_maths} \net notes_physiques: \n{notes_physiques}")

print(f"La moyenne de notes_maths: {np.mean(notes_maths)} et de notes_physiques: {np.mean(notes_physiques)}\n")
print(f"L'ecart-type de notes_maths: {np.std(notes_maths)} et de notes_physiques: {np.std(notes_physiques)}\n")
print(f"La mediane de notes_mats: {np.median(notes_maths)} et de notes_physiques: {np.median(notes_physiques)}\n")

# Mporeis na arxikopoieis se mia grammi

notes_combined = np.concatenate([notes_maths,notes_physiques], axis=None)
print(f"La concatenation de matrices est: {notes_combined}\n")

# Enregistrez le tableau notes_combined dans un fichier CSV
# create a dictionary


# Create the file and write
# edw tha  borouses na xrhsimopoiohseis thn bibliothiki pandas

import csv
with open('notes_combined.csv','w', newline='') as fichier:
    colonnes=['Maths', 'Physique']
    ecrivain = csv.DictWriter(fichier,fieldnames=colonnes)
    ecrivain.writeheader()
    notes = {'Maths':0, 'Physique':0}
    print("notes empty list --------------\n",notes)
    for i in range(0,len(notes_combined)-1,2):
        if i <= 20:
            notes.update([('Maths', notes_combined[i])])
        else:
            notes.update([('Physique', notes_combined[i])])
        

    print("notes FULL list --------------\n",notes)
    print("notes in DICTIONARY:\n", notes)
    for note in notes:    
        ecrivain.writerow(note)

# 
mentions = np.arange(len(notes_combined),dtype=int)
for i,elem in enumerate(notes_combined):
    if elem > 16:
        mentions[i] = True
    else:
        mentions[i] = False
print(f"Le tableau mentions: \n {mentions}")
# se mia grammi 
# mentions = notes_combined >=16

#
etudiants_meritants = np.zeros(len(notes_combined),dtype=int)
sum1 = 0
for i,elem in enumerate(notes_combined):
    if mentions[i]:
        etudiants_meritants[i] = notes_combined[i]
        sum1 +=1
print("Le tableau etudiants_meritants: \n", etudiants_meritants)
print(f"le pourcentage est: { 100*sum1/len(notes_combined) } % ")

#
print("\nLes valeurs qui sont inferieurs de 15:")
for i,elem in enumerate(notes_combined):
    if i > 15:
        print(i)
    if elem > 14 :
        notes_combined[i] = 14
# se enallaktiki
# indices_sup_15 = no.where(notes_combined > 15)

print("Le notes combined apres remplacement: \n", notes_combined)
"""
#act3

#act4

#act5

import tkinter as tk 
# Étape 1: Définir la classe Contact 
class Contact: 
    def __init__(self, nom, numero):
        self.nom = nom 
        self.numero = numero 
    def __str__(self): return f"{self.nom} - {self.numero}" 
# Étape 2: Créer la classe CarnetAdresses 
class CarnetAdresses: 
    def __init__(self):
        self.contacts = [] 
    def ajouter_contact(self, contact):
        self.contacts.append(contact)
    def get_liste_contacts(self): 
        return self.contacts
    
# Étape 3: Construire l'interface utilisateur avec Tkinter 
class Application(tk.Tk): 
    def __init__(self): 
        super().__init__() 
        self.title("Carnet d'Adresses") 
        self.carnet = CarnetAdresses() #instantiation of CarnetAdress so that we can use it after
        tk.Label(self, text="Nom:").pack() 
        self.nom_entry = tk.Entry(self) 
        self.nom_entry.pack() 
        tk.Label(self, text="Numéro:").pack() 
        self.numero_entry = tk.Entry(self) 
        self.numero_entry.pack() 
        self.ajouter_btn = tk.Button(self, text="Ajouter", command=self.ajouter_contact) 
        self.ajouter_btn.pack() 
        self.contacts_text = tk.Text(self, height=10, width=50) 
        self.contacts_text.pack()

    def ajouter_contact(self): 
        nom = self.nom_entry.get() 
        numero = self.numero_entry.get() 
        if nom and numero: # Vérifier que les champs ne sont pas vides 
            contact = Contact(nom, numero) 
            self.carnet.ajouter_contact(contact) 
            self.mettre_a_jour_affichage() 
            self.nom_entry.delete(0, tk.END) 
            self.numero_entry.delete(0, tk.END) 
    def mettre_a_jour_affichage(self): 
        self.contacts_text.delete(1.0, tk.END) # so that the entries get updated after adding
        for contact in self.carnet.get_liste_contacts(): 
            self.contacts_text.insert(tk.END, str(contact) + "\n") 
# Fonction d'exécution 
def main(): 
    app = Application() 
    app.mainloop()

if __name__ == "__main__": 
    main()