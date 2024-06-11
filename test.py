nom = input('Quel est vôtre nom? ')
age = input("Quel est vôtre âge? ")

try:
    age_prochain = int(age) + 1
except:
    print("ERREUR! Vous devez entrer un nombre")
else:
    print(f"Vous vous appelez {nom}. Vous avez {int(age)} ans et l'an prochain, vous aurez {age_prochain} ans")