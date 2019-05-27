class Nodo:
    def __init__(self, valor, hijos = []):
        self.valor = valor
        self.hijos = hijos

def buscar(arbol, valor):
    if arbol == None:
        return False
    if arbol.valor == valor:
        return True
    return buscarHijos(arbol.hijos, valor)

def buscarHijos(hijos, valor):
	if hijos == []: return False
	return buscar(hijos[0], valor) or buscarHijos(hijos[1:], valor)

def a_lista(arbol):
    if arbol == []:
        return []
    if len(arbol.hijos)==1:
        return a_lista( [arbol.valor] +  a_lista(arbol.hijos[0]))
    return a_lista( [arbol.valor])+ a_lista(arbol.hijos[1:])

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

arbol = Nodo(25, [Nodo(10, []),Nodo(40, [])])
print buscar(arbol, 12)
a_lista(arbol)

