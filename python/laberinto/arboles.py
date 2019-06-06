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

def arbol_lista(arbol):
    #print (arbol.valor)
    if arbol == None:
        #return []
        return []
    print ('arbol', arbol.valor)
    return [arbol.valor] + hijos_lista(arbol.hijos)

def hijos_lista(hijos):
    if hijos == []:
        return []
        #return None
    if len(hijos) == 1:
        return arbol_lista(hijos[0])
    return arbol_lista(hijos[0]) + hijos_lista(hijos[1:])

#Albol ya tiene raiz
def insertar(arbol, padre ,valor):
    print ('No es Padre: ', arbol.valor)
    if arbol == None:
        print ('Vacio')
        return arbol
    if arbol.valor == padre:
        #print ('Es Padre: ', arbol.valor)
        arbol.hijos.append(valor)
        print (arbol.hijos)
        return Nodo(arbol.valor, arbol.hijos)
    #print arbol_lista(Nodo(arbol.valor, arbol.hijos))
    return Nodo(arbol.valor, insertarEnHijos(arbol.hijos, padre, valor))

def insertarEnHijos(hijos, padre, valor):
    #print ('hijos')
    if len(hijos) < 1:
        print ('hijos Vacio')
        return []
    return [insertar(hijos[0], padre, valor)] + [insertarEnHijos(hijos[1:], padre, valor)]


arbol = Nodo(25, [Nodo(10, [Nodo(12, [])]), Nodo(40, [Nodo(36, [])]), Nodo(50, [Nodo(27, [])]) ] )

#print (buscar(arbol, 28))
print (arbol_lista(arbol))
arbol = insertar(arbol, 27, 8)
print (arbol_lista(arbol))
