# Laberinto usando arboles n-arios

Presentado Por:

   - Nicolas Mendigaño
   - Jeison Jara

Se implementa un programa, que dado un archivo .txt que contiene un averinto compuesto por 1s y 0s (1 representa paredes y 0 camino), X que indica el inicio e Y que indica donde se debe llegar, cargarlo y encontrar si hay una solucion para llegar de X a Y

El arbol n-ario debe ser insertado como:
```
arbol = Nodo(25, [Nodo(10, [Nodo(12, [])]), Nodo(40, [Nodo(36, [])]), Nodo(50, [Nodo(27, [])]) ] )
```
Para el manejo del problema se hace uso de las sigugiente funciones para arboles n-arios.

## Nodo

Cada nodo esta conformado por su valor, y una lista de hijos.

```
class Nodo:
    def __init__(self, valor, hijos = []):
        self.valor = valor
        self.hijos = hijos
```

## Buscar
Busca un valor indicado en el arbol.
```
def buscar(arbol, valor):
    if arbol == None:
        return False
    if arbol.valor == valor:
        return True
    return buscarHijos(arbol.hijos, valor)

def buscarHijos(hijos, valor):
    if hijos == []: return False
    return buscar(hijos[0], valor) or buscarHijos(hijos[1:], valor)

```


## Listar arbol
Muestra una lista de los valores que contiene el arbol
```
def arbol_lista(arbol):
    if arbol == None:
        return []
    return [arbol.valor] + hijos_lista(arbol.hijos)

def hijos_lista(hijos):
    if hijos == []:
        return []
    return arbol_lista(hijos[0]) + hijos_lista(hijos[1:])
```

## Insertar valor
Inserta el valor que se indique en el arbol
```
def insertar(arbol, padre ,valor):
    if arbol == None:
        return arbol
    if arbol.valor == padre:
        arbol.hijos.append(valor)
        return Nodo(arbol.valor, arbol.hijos)
    return Nodo(arbol.valor, insertarEnHijos(arbol.hijos, padre, valor))

def insertarEnHijos(hijos, padre, valor):
    if hijos == []:
        return []
    return [insertar(hijos[0], padre, valor)] + [insertarEnHijos(hijos[1:], padre, valor)]

```
