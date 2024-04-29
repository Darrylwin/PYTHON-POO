def supp(chaine):
    for voy in range(len(chaine) + 1):
        if chaine[voy] in "aoieu":
            chaine[voy] = ""
    return chaine


# Programme principal

print(supp(" Ce site est pour les perdants LOL ! "))
