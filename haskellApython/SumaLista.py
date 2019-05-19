def sumalista(listaNumeros):
    if len(listaNumeros) == 0:
        return 0
    elif len(listaNumeros) == 1:
        return listaNumeros[0]
    else:
        return listaNumeros[0] + sumalista(listaNumeros[1:])

print(sumalista([]))
