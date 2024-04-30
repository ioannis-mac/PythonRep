import datetime, os, platform
import subprocess as sub

# ----- LINUX ------
def maintenanceLINUX():
    try:
        #clean temp files
        result = sub.run(['sudo','rm', '-r', '/tmp'], capture_output=True, text=True)
        print("--------------------- Result est: \n", result)
        return str(result)
    except sub.CalledProcessError:
        result = "Une erreur a eu lieu\n"
    return result

def mis_a_jour_systemLINUX():
    resultatTotal = ''
    try:
        resultat1 = sub.run(['sudo', 'apt-get', 'update'], capture_output=True, text=True)
        resultat2 = sub.run(['sudo', 'apt-get', 'upgrade', '-y'], capture_output=True, text=True)
        resultatTotal = str(resultat1.stdout) + str(resultat2.stdout)
    except sub.CalledProcessError:
        resultatTotal = "Une erreur a eu lieu\n"
    return resultatTotal

def verifier_integriteLINUX():
    resultat = ''
    try:
        resultatTotal = sub.run(['fsck'], capture_output=True, text=True)
        return str(resultatTotal)
    except sub.CalledProcessError:
        resultatTotal = "Une erreur a eu lieu\n"
    return resultatTotal


# ----- WINDOWS -----
def mis_a_jour_systemWINDOWS():
    #Update Windows
    print("Windows")

if __name__ == "__main__":
    nom_fichier = "Report.txt"
    
    result = sub.run(['ls','-l'],capture_output=True, text=True)

    if nom_fichier not in result.stdout: # Si il n'existe pas, creer
        with open(nom_fichier, "+x") as fichier:
            fichier.close()
    else:
        with open(nom_fichier, "w") as fichier:
            # absolute file positioning 
            fichier.seek(0)  
    
            # to erase all data inside
            fichier.truncate()
            fichier.close()
    
    with open(nom_fichier, "w") as fichier:
        start_time = datetime.datetime.now()
        fichier.write(f"###### Bienvenue dans le rapport de votre machine. La date est {start_time} ####### \n")

        systemNow = platform.system()
        if systemNow == 'Linux':
            # Mettre a jour
            resultatMettreAJour = mis_a_jour_systemLINUX()
            fichier.write("\n\n ----- Le logiciel du systeme est mis a jour ----- \n")
            fichier.write(str(resultatMettreAJour))

            # Maintenance
            resultatMaintenance = maintenanceLINUX()
            fichier.write("\n\n ----- Les fichiers temporaires du systeme sont nettoye ----- \n")
            fichier.write(resultatMaintenance)

            # Verifier l'integrite du systeme
            resultatVerification = verifier_integriteLINUX()
            fichier.write("\n\n ----- La verification du system est termine ------\n")
            fichier.write(resultatVerification)

        elif systemNow == 'Windows':
            mis_a_jour_systemWINDOWS()
            # Et les autres

        elif systemNow == "macOS":
            print('Il faut trouver les commandes')
        fichier.close()