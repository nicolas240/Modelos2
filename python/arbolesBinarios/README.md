# Manejo Arboles Binarios

Presentado Por:

    -Nicolas Mendigaño
    -Jeison Jara

Funciones para el manejo basico de arboles binarios.

## Nodo

Cada nodo esta conformado por su valor, un arbol por izquierda y un arbol por derecha.

```
class Nodo:
    def __init__(self, valor, izq = None, der = None):
        self.valor = valor
        self.izq = izq
        self.der = der
```
