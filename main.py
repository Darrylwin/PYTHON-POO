# coding: utf-8
compteur = 0
while compteur < 20:
    print(compteur * "£")
    compteur += 1
from math import sqrt

print("Entrer trois variables a , b et c tel qu'on ait ax^2 + bx + c  0")
a = int(input("Entrer a: "))
b = int(input("Entrer b: "))
c = int(input("Entrer c: "))
dis = b ** 2 - 4 * a * c
if dis == 0:
    print(f"On a une solution x0 tel que x0 = {int((-b / 2 * a))}")
elif dis > 0:
    print(
        f"On a deux solutions x1 et x2 tel que x1 = {int((-b - sqrt(dis)) / 2 * a)} et x2 = {int((-b + sqrt(dis)) / 2 * a)}")
else:
    print(f"On a pas de solution")

from math import factorial as fac

print('Voila la factorielle :', fac(b))
