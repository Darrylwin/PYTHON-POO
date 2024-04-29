# Demander la taille du tableau (nombre de lignes et de colonnes)
nb_lignes, nb_colonnes = int(input("Saisissez le nombre de lignes : ")), int(
    input("Saisissez le nombre de colonnes : "))

# Créer un tableau vide (liste de listes) et saisir les données
for j in range(nb_colonnes +1):
    for i in range(nb_lignes +1):
        tableau = [[input(f"Saisissez la valeur pour l'élément ({i}, {j}) : ")]]


# Afficher le tableau
for ligne in tableau:
    print(ligne, end="")
