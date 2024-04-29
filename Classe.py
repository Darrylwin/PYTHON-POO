class Humain:
    perso_cre = 0

    def __init__(self):
        self.nom = input("Entrer le nom du Perso :")
        self.age = input("Entrer l'age du Perso :")
        print(f"Création du Personnage {self.nom}... agé de {self.age} ans")
        Humain.perso_cre += 1
        print(f"Nomre de perso créés: {Humain.perso_cre}")

#Programme Principal


print("Lancement du programme ...")

H1 = Humain()
print(f"Nom de Personnage : {H1.nom}")
H2 = Humain()
print(f"Nom de personnae : {H2.nom}")
