class Nodo:
    def __init__(self, valor, izq = None, der = None):
        self.valor = valor
        self.izq = izq
        self.der = der

def buscar(arbol, valor):
    if arbol == None:
        return False
    if arbol.valor == valor:
        return True
    if arbol.valor < valor:
        return buscar(arbol.der, valor)
    if arbol.valor > valor:
        return buscar(arbal.izq, valor)

def sumar(arbol):
    if arbol == None:
        return 0
    return sumar(arbol.izq) + arbol.valor + sumar(arbol.der)

def a_lista(arbol):
    if arbol == None:
        return []
    return a_lista(arbol.izq) + [arbol.valor] + a_lista(arbol.der)

def insertar(arbol, valor):
    if arbol == None:
        return Nodo(valor)
    if arbol.valor < valor:
        return Nodo(arbol.valor, arbol.izq, insertar(arbol.der, valor))
    return Nodo(arbol.valor, insertar(arbol.izq, valor), arbol.der)

def crearArbol(arbol, lista):
    if lista == []:
        return arbol
    if len(lista) > 0:
        return crearArbol(insertar(arbol, lista[0]), lista[1:])
    

lista = [25, 40, 18, 5, 50, 10]
print a_lista(crearArbol(Nodo(None),lista))

"""
arbol = Nodo(25, Nodo(10, Nodo(5), Nodo(18)), Nodo(40, None, Nodo(50)))

#Lista
print "Arbol: "
print a_lista(arbol)

#Insertar
print "Insertando valor: "
arbol = insertar(arbol, 12)
print a_lista(arbol)

#Sumar
print "Suma del arbol: "
print sumar(Nodo(25, Nodo(10, Nodo(5), Nodo(18)), Nodo(40, None, Nodo(50))))

#Buscar
print "Busqueda de valor: "
print buscar(Nodo(25, Nodo(10, Nodo(5), Nodo(18)), Nodo(40, None, Nodo(50))), 50)

"""

