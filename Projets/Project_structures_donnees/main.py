import os,csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class GestionEtudiants:
    def __init__(self,donnesEtudiants):
        self.donnesEtudiants = donnesEtudiants

    def ajouter_donnes(self, note):
        self.donnesEtudiants.append(note)
        print(f"Ajoute {note}\n")

    def supprimer_donnees(self, note):
        self.donnesEtudiants.remove(note)

    def affichage_donnes(self):
        print("Les etudiants ils sont:", self.donnesEtudiants)


class GestionCours:
    def __init__(self,donnesCours):
        self.donnesCours = donnesCours

    def ajouter_donnes(self, note):
        self.donnesCours.append(note)
        print(f"Ajoute {note}\n")

    def supprimer_donnees(self, note):
        self.donnesCours.remove(note)

    def affichage_donnes(self):
        print("Les cours ils sont:", self.donnesCours)

if __name__ == "__main__":

    # Etudiants
    e1 = GestionEtudiants([])
    Etudiant = ["Boby","Bob",1, 10,9]
    Etudiant2 = ["Papadopoulou","Nefeli",  2, 5,9]
    Etudiant3 = ["Andrianou","Veroniki", 3, 2,7]
    e1.ajouter_donnes(Etudiant)
    e1.ajouter_donnes(Etudiant2)
    e1.ajouter_donnes(Etudiant3)
    e1.affichage_donnes()
    e1.supprimer_donnees(Etudiant)
    e1.affichage_donnes()

    # Cours
    c1 = GestionCours([])
    Cours1 = ["Math", 9879, "Dimitris"]
    Cours2 = ["Informatique", 9879, "Andreas"]

    c1.ajouter_donnes(Cours1)
    c1.ajouter_donnes(Cours2)


    # Gestion des notes
    print("-------- Gestion des notes ------")
    # Je peux creer un .csv pour ca

    #Create the file and write
    os.remove("NotesDeCours.csv")
    with open('NotesDeCours.csv','+x', newline='') as fichier:
        colonnes=['Math', 'Informatique']
        ecrivain = csv.DictWriter(fichier, fieldnames=colonnes)
        ecrivain.writeheader()
        for i in range(len(e1.donnesEtudiants)):
            aTempDict={"Math":e1.donnesEtudiants[i][3], "Informatique":e1.donnesEtudiants[i][4]}
            print(aTempDict)
            ecrivain.writerow(aTempDict)
    with open('NotesDeCours.csv', "r")as fichier:
        lecteur = csv.DictReader(fichier)
        for ligne in lecteur:
            print(ligne)

    # Creation de DataFrames avec pandas
    students_df = pd.DataFrame(e1.donnesEtudiants)
    courses_df = pd.DataFrame(c1.donnesCours)
    notes = np.random.randint(0, 21, size=(len(e1.donnesEtudiants), len(c1.donnesCours)))
    grades_df = pd.DataFrame(notes, index=[Etudiant[3] for Etudiant in e1.donnesEtudiants], columns=[c[0] for c in c1.donnesCours])

    print("students DataFrame\n",students_df)
    print("courses DataFrame\n", courses_df)
    print("notes DataFrame\n", notes)
    print("grades DataFrame\n", grades_df)

    # ---------- Moyennes et mediane -----------
    moyennes_par_etudiant = grades_df.mean(axis=1) 
    medianes_par_etudiant = grades_df.median(axis=1)
    print("moyennes Etudiants: \n", moyennes_par_etudiant)
    print("medianes Etudiants: \n",medianes_par_etudiant)

    # ---------- PLOT ------------
    plt.figure(figsize=(10, 6))
    print("students_df[2]\n", students_df[2])
    plt.bar(students_df[2], moyennes_par_etudiant, color='skyblue')
    plt.xlabel('Numéro d\'étudiant')
    plt.ylabel('Moyenne des notes')
    plt.title('Moyenne des notes par étudiant') 
    plt.xticks(rotation=45) 
    plt.tight_layout() 
    plt.show()