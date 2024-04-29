def saisir(nb_line, nb_col):
    global tab
    for i in range(nb_line + 1):
        for j in range(nb_col + 1):
            tab = [[input(f"Entrer l'élément [{j + 1}][{i + 1}]:")]]
    for line in tab:
        print(line, end=" ")


print(saisir(1, 2))
