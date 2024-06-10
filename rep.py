def menu():
    print(' 0-quitter \n 1-écrire dans le répertoire  \n 2-rechercher dans le repertoir')#on écrit les choix possibles à l'utilisateur
    numero= int(input('Votre choix ?'))#on demande à l'utilisateur de choisir un nombre affectué à une commande
    if numero==0:#on dessine le chemin que prendra l'utilisatuer en choisissant sont numéros.Si il execute 0 la cellule se termine
        quit()
    elif numero==1:#Si l'utilisateur execute 1. La fonction l'envoie sur la fonction écriture
        ecriture()
    elif numero==2:#Si l'utilisateur execute 2. La fonction l'envoie sur la fonction lecture
        lecture()
    else:
        print('\n erreur! Choisissez entre les propositions ci-dessous\n')
        menu()
        
def ecriture():
    with open("repertoire.txt","a") as f: #la fonction ouvre un fichier txt que l'on nomme repertoire
      reponse=input("Nom (0 pour terminer) :")
      if reponse!="0":
           reponse1=input("Téléphone : ")#demande à l'utilisateur un numéro de téléphone
           f.write(reponse)#écrit le nom dans le fichier
           f.write(" ")#on fait un espace entre le nom et le numéro de téléphone
           f.write(reponse1)#écrit le numéro de téléphone dans le fichier
           f.write("\n")#revient à la ligne après l'écriture du numéro
           ecriture()
      elif reponse=="0":#retourne au menu après avoir écrit 0
           menu()

       
def lecture():
    nom=input("Entrez un nom :")#demande à l'utilisateur un nom et la fonction donnera le numero de téléphone si il existe
    with open("repertoire.txt","r") as f:#on ouvre le fichier juste avec le droit
        for ligne in f :
            reponse=ligne.split(" ") # on sépare le nom et le numéro de téléphone
            if reponse[0]==nom:# si l'utilisateur cherche un nom et qu'il le retrouve dans le fichier il écrit le numéro de téléphone
                print("Le numéro recherché est :",reponse[1])
                return menu()#on retourne au menu
        print("Inconnu\n")#la fonction écrit inconnu si le nom ni le numéro n'existe pas
        menu()#puis il retourne au menu
