if __name__ == '__main__':
    # Question I
    # Creation d'une liste de 10 elements de type chaîne de caractères
    animaux = ["chat", "chien", "souris", "oiseau", "poisson", "cheval", "vache", "mouton", "cochon", "lapin"]
    
    # 1- Affichage des elements de la liste
    print("1) Affichage des elements de la liste")
    print("--------------------------------------------------")
    print(animaux)
    print("--------------------------------------------------\n")
    
    # 2- Changer le contenu de l'element numero 5
    print("2) Changement du contenu de l'element numero 5")
    print("--------------------------------------------------")
    animaux[4] = "requin"
    print(animaux)
   
    #3- Creation d' une nouvelle liste
    nouvelle_liste = []
    # remplissage avec les elements de la liste precedente contenant la lettre "a"
    for element in animaux:
        if "a" in element:
            nouvelle_liste.append(element)
    print("\n3) les elements de la liste contenant la letter a:")
    print("--------------------------------------------------")
    print(nouvelle_liste)
    
    #4 Ajout d'un element a la fin de la liste
    print("\n4) Ajout d'un element a la fin de la liste")
    print("--------------------------------------------------")
    animaux.append("tortue")
    print(animaux)
    
    # #5 Ajout d'un element a l'index numero 2
    print("\n5) Ajout d'un element a l'index numero 2")
    print("--------------------------------------------------")
    animaux.insert(2, "serpent")
    print(animaux)

    # #6 Suppression de l'element numero 3
    print("\n6) Suppression de l'element numero 3")
    print("--------------------------------------------------")
    animaux.remove("souris")
    print(animaux)
    
    # #7. Suppression l'element a l'index numero 2
    print("\n7) Suppression de l'element a l'index numero 2")
    print("--------------------------------------------------")
    del animaux[2]
    print(animaux)
    
    # #8 Ordonner la liste
    print("\n8) Ordonnancement de la liste")
    print("--------------------------------------------------")
    animaux.sort()
    print(animaux)
 
    # #9 Afficher le sens au sens inverse
    print("\n9) Affichage dans le sens inverse")
    print("--------------------------------------------------")
    animaux.reverse()
    print(animaux)
    
    # #10 Vider la liste
    print("\n10) Vidange de la liste")
    print("--------------------------------------------------")
    animaux.clear()
    print(animaux)
    
    # #11 Suppression de la liste
    del animaux

    # Question 2
    print("==========Question 2============")
    # Creation d' une tuple de 10 elements de type entier
    chiffre = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    
    # Affichage des elements de la tuple chiffre
    print("\nAffichage des elements de la tuple")
    print("--------------------------------------------------")
    print(chiffre)
    
    #1) Affichage du nombre de fois que valeur 3 apparait dans la tuple chiffre
    print("\n1) Affichage du nombre de fois que valeur 3 apparait dans la tuple")
    print("--------------------------------------------------")
    print(chiffre.count(3))

    #2) Affichage du contenu de l'element numero 5
    print("\n2) Affichage du contenu de l'element numero 5")
    print("--------------------------------------------------")
    print(chiffre[4])
    
    #3) Ordonnancement du tuple
    print("\n3) Ordonnancement du tuple")
    print("--------------------------------------------------")
    chiffre = tuple(sorted(chiffre))
    print(chiffre)
    
    #4) Ajout d' un element a la fin de la tuple
    print("\n4) Ajout d' un element a la fin de la tuple")
    print("--------------------------------------------------")
    # On ne peut pas modifier une tuple directement, il faut creer une nouvelle tuple
    liste = list(chiffre)
    # Ajouter un element a la fin de la liste
    liste.append(4)
    # Reconvertir la liste en tuple
    chiffre = tuple(liste)
    # Affichage du nouveau tuple 
    print(chiffre) 
    
    #5) Ajouter un element a l'index numero 3
    print("\n5) Ajouter un element a l'index numero 3")
    print("--------------------------------------------------")
    # On ne peut pas modifier une tuple directement, il faut creer une nouvelle tuple
    chiffre = chiffre[:3] + (12,) + chiffre[3:]
    print(chiffre)

    #6) Affichage de la nouvelle tuple
    print("\n6) Affichage de la nouvelle tuple")
    print("--------------------------------------------------")
    print(chiffre)
  
    # Question 3
    print("==========Question 3============")
    # Creation d'un set de 10 elements de type chaine de caractères
    salutation = {"Bonjour", "Hello", "Hola", "Salut", "Hi", "Ciao", "Ola", "Aloha", "Namaste", "Salam"}

    #1 Affichage du set
    print("\n1) Affichage du set")
    print("--------------------------------------------------")
    print(salutation)
    
    #2 Ajouter un element
    print("\n2) Ajout d'un element dans le set")
    print("--------------------------------------------------")
    salutation.add("Shalom")
    print(salutation)

    #3 Supprimer un element
    print("\n3) Suppression d'un element dans le set")
    print("--------------------------------------------------")
    salutation.remove("Hola")
    print(salutation)
    
    #4 Supprimer le set
    print("\n4) Suppression du set")
    print("--------------------------------------------------")
    del salutation
    
     # Question 4
    print("==========Question 4============")
    # Creation d' un dictionnaire de 10 elements de type chaîne de caractères
    chiffres = {"1": "un", "2": "deux", "3": "trois", "4": "quatre", "5": "cinq", "6": "six", "7": "sept", "8": "huit", "9": "neuf", "10": "dix"}
    
    #1 Affichage du dictionnaire
    print("\n1) Affichage du dictionnaire")
    print("--------------------------------------------------")
    print(chiffres)
    
    #2 Affichage seulement des cles
    print("\n2) Affichage des cles seulement")
    print("--------------------------------------------------")
    print(chiffres.keys())
    
    #3 Affichage seulement des valeurs
    print("\n3) Affichage des valeurs seulement")
    print("--------------------------------------------------")
    print(chiffres.values())
    
    #4 Afficher les cles et les valeurs sous le format : Cle : Valeur
    print("\n4) Affichage des cles et des valeurs sous le format: k:v")
    print("--------------------------------------------------")
    for cle, valeur in chiffres.items():
        print(f"{cle} : {valeur}")

    #5 Supprimer l'element a la cle numero 2
    print("\n5) Supprimer l'element a la cle numero 2")
    print("--------------------------------------------------")
    chiffres.pop("2")
    print(chiffres)
    
    #6 Afficher l'element de la cle numero  5
    print("\n6) Affichage de l'element de la cle numero 5")
    print("--------------------------------------------------")
    print(chiffres["5"])

    #7 Ajouter un nouvel element
    print("\n7) Ajout d'un nouvel element")
    print("--------------------------------------------------")
    chiffres["11"] = "onze"
    print(chiffres)
    
    #8 Creer une copie du dictionnaire
    print("\n8) Creation d'une copie du dictionnaire")
    print("--------------------------------------------------")
    copie_dict = chiffres.copy()
    print(copie_dict)
        
    #9 Afficher les nouveaux elements
    print("\n9) Affichage des nouveaux elements")
    print("--------------------------------------------------")
    print(copie_dict)
