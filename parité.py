def paire(nombre):
    """
    :param nombre: entier positif
    :return: True the nombre is paire 😄
    """
    if nombre % 2 == 0:
        return "Le nombre est paire"
    elif nombre % 2 == 1:
        return "Le nombre est impaire"


print(paire(9))

from math import cos, pi

print(cos(pi / 2j))

from math import sqrt, pi, sin


class Human:
    def __init__(self):
        self.name = "Albert"
        self.age = 21
        print(self.name)


F1 = Human()
