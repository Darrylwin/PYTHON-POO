
# Creation de la classe Voiture
class Voiture:

    marque = input("Veuillez saisir la marque de la bagnole : ")
    couleure = input("Veuillez saisir la couleure de la bagnole : ")
    puissance = input("Veuillez saisir le nombre de chevaux de la bagnole : ")


"""  Programme Principal   """

# Instanciation de la classe Voiture

voiture_1 = Voiture()
voiture_2 = Voiture()
voiture_3 = Voiture()

print(voiture_1.marque)
print(voiture_2.couleure)
print(voiture_3.puissance)

# changement de l'attribut "marque" de la classe Voiture

Voiture.marque = "Porshe"

print(voiture_1.marque)

# Attribution de nouvelles valeures aux instances de la Classe

voiture_1.marque = " Alpha Roméo"
voiture_2.marque = "Ferrari"
voiture_3.puissance = 800

print(voiture_1.marque)
print(voiture_2.marque)
print(voiture_3.puissance)
