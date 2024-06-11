# Demander la taille du tableau (nombre de lignes et de colonnes)
nb_lignes, nb_colonnes = int(input("Saisissez le nombre de lignes : ")), int(
    input("Saisissez le nombre de colonnes : "))
# tableau = []
# Créer un tableau vide (liste de listes) et saisir les données
# for j in range(nb_colonnes +1):
#     for i in range(nb_lignes +1):
#         tableau.append([input(f"Saisissez la valeur pour l'élément ({i}, {j}) : ")])

tableau = [input(f"Saisissez la valeur pour l'élément ({x}, {y}) : ") for x in range(nb_lignes+1) for y in range(nb_colonnes+1)]

# Afficher le tableau
for ligne in tableau:
    print(ligne, end=" ")
