# Definition de la classe Voiture
class Voiture:
    # Attribut de classse
    voiture_crees =0
    def __init__(self, marque, couleure, puissance):
        self.marque = marque
        self.couleure = couleure
        self.puissance = puissance
        Voiture.voiture_crees += 1


# Programmeprincipal
voiture_1 = Voiture("BUGATTI", "CELTIC", 1600)
voiture_2 = Voiture("Koenigsegg", "GRIS-NARDOW", 2000)

print(voiture_1.marque)
print(voiture_1.couleure)
print(voiture_1.puissance)

print("")

print(voiture_2.marque)
print(voiture_2.couleure)
print(voiture_2.puissance)

print("")

print(f"Nombre de voituures crées : {Voiture.voiture_crees} ")