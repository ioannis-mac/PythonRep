
import csv

monfichier = open("text.txt", "x")
monfichier.write("Bonjour")
monfichier.close()

fichier = open("text3.txt", "x")
ecrivain=csv.writer(fichier)