# Manejo Arboles Binarios

Presentado Por:

   - Nicolas Mendigaño
   - Jeison Jara

Funciones para el manejo basico de arboles binarios.

El arbol debe ser insertado como:
```
arbol = Nodo(25, Nodo(10, Nodo(5), Nodo(18)), Nodo(40, None, Nodo(50)))
```
## Nodo

Cada nodo esta conformado por su valor, un arbol por izquierda y un arbol por derecha.

```
class Nodo:
    def __init__(self, valor, izq = None, der = None):
        self.valor = valor
        self.izq = izq
        self.der = der
```

## Buscar
Busca un valor indicado en el arbol.
```
def buscar(arbol, valor):
    if arbol == None:
        return False
    if arbol.valor == valor:
        return True
    if arbol.valor < valor:
        return buscar(arbol.der, valor)
    if arbol.valor > valor:
        return buscar(arbal.izq, valor)
```

## Sumar
Suma todos los valores que contiene el arbol
```
def sumar(arbol):
    if arbol == None:
        return 0
    return sumar(arbol.izq) + arbol.valor + sumar(arbol.der)
```

## Listar arbol
Muestra una lista de los valores que contiene el arbol
```
def sumar(arbol):
    if arbol == None:
        return 0
    return sumar(arbol.izq) + arbol.valor + sumar(arbol.der)
```

## Insertar valor
Inserta el valor en que se indique en el arbol
```
def insertar(arbol, valor):
    if arbol == None:
        return Nodo(valor)
    if arbol.valor < valor:
        return Nodo(arbol.valor, arbol.izq, insertar(arbol.der, valor))
    return Nodo(arbol.valor, insertar(arbol.izq, valor), arbol.der)
```

## Crear arbol a partir de lista lista
Si se tiene una lista de este tipo:
```
lista = [25, 40, 18, 5, 50, 10]
```
Se creara un arbol que tiene como raiz al primer elemento de la lista.
```
def crearArbol(arbol, lista):
    if lista == []:
        return arbol
    if len(lista) > 0:
        return crearArbol(insertar(arbol, lista[0]), lista[1:])
```
