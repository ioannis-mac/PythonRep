import subprocess as sub

def create_file(fichier):
    result = sub.run(['touch', fichier], capture_output=True, text=True) # type: ignore

def list_files():
    result = sub.run(['ls', '-l'], capture_output=True, text=True) # type: ignore
    return result

def delete_file(fichier):
    result = sub.run(['rm', fichier], capture_output=True, text=True) # type: ignore

def append_to_file(fichier, chaine):
    with open(fichier,"+x") as output_file:
       result = sub.run(['echo', chaine], stdout=output_file) # type: ignore

nom_fichier = "JeVoudraisDormir.py"
create_file(nom_fichier)
list_files()
delete_file(nom_fichier)

nom_fichier1 = "JeVoudraisDormirDePlus.py"
chaine="Et avoir un bon repose"
append_to_file(nom_fichier1, chaine)