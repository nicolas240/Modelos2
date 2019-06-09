#!bin/python2.7

import functools

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
    #print ('arbol', arbol.valor)
    return [arbol.valor] + hijos_lista(arbol.hijos)

def hijos_lista(hijos):
    if hijos == []:
        return []
        #return None
    return arbol_lista(hijos[0]) + hijos_lista(hijos[1:])

#Albol ya tiene raiz
def insertar(arbol, padre ,valor):
    if arbol == None:
        return arbol
    if arbol.valor == padre:
        arbol.hijos.append(Nodo(valor, []))
        return Nodo(arbol.valor, arbol.hijos)
    return Nodo(arbol.valor, insertarEnHijos(arbol.hijos, padre, valor))

def insertarEnHijos(hijos, padre, valor):
    if hijos == []:
        return []
    return [insertar(hijos[0], padre, valor)] + insertarEnHijos(hijos[1:], padre, valor)

def recorrer(f,arbol,fila,columna):
      	"""Un if para mirar si hay dos raices o dos puntos de llegada """
        if(len(filter(lambda x: x=='x',functools.reduce(lambda x,y: x+y, f) ))!=1 or len(filter(lambda x: x=='y', functools.reduce(lambda x,y: x+y, f) ))!=1):
                return False
	padre=arbol.valor
	print ('fila:',fila, 'columna: ',columna)
	if(f[fila][columna]==1 or f[fila][columna]==None):return False
	arbol=insertar(arbol,padre,arriba(f,fila,columna))
	if  f[fila-1][columna]!='1': recorrer(f,arbol,fila-1,columna)#f[fila-1][columna]!=None and
	arbol=insertar(arbol,padre,abajo(f,fila,columna))
	if  not fila+2>len(f) and f[fila+1][columna]!='1': recorrer(f,arbol,fila+1,columna)

        arbol=insertar(arbol,padre,derecha(f,fila,columna))
	if not columna+2<len(f[fila]) and f[fila][columna+1]!='1': recorrer(f,arbol,fila,columna+1)

        arbol=insertar(arbol,padre,izquierda(f,fila,columna))
	if not columna-1<0 and f[fila][columna-1]!='1': recorrer(f,arbol,fila,columna-1)

	#recorrer(f,arbol,fila,columna-1)
	return buscar(arbol,-2)

def arriba(f, fila, columna):
        if fila-1<0: return None
        if f[fila-1][columna]=='y':
                f[fila-1]= f[fila-1][:columna-1]+\
                        '1'+f[fila-1][columna+1:]
                return -2
        if f[fila-1][columna]=='0':
                f[fila-1]= f[fila-1][:columna-1]+\
                        '1'+f[fila-1][columna+1:]
                return (fila-1)*len(f[fila])+columna+1
        return None
#columna+1 por la posicion 0

def abajo(f, fila, columna):
        if fila+2>len(f): return None
        if f[fila+1][columna]=='y':
                f[fila+1]=f[fila+1][:columna-1]+\
                        '1'+f[fila+1][columna+1:]
                return -2
        if f[fila+1][columna]=='0':
                f[fila+1]=f[fila+1][:columna-1]+\
                        '1'+f[fila+1][columna+1:]
                return (fila+1)*len(f[fila])+columna+1
        return None

def derecha(f,fila,columna):
        if columna+2>len(f[fila]): return None
        if f[fila][columna+1]=='y':
                f[fila]= f[fila][:columna]+\
                        '1'+f[fila][columna+2:]
                return -2
        if f[fila][columna+1]=='0':
                f[fila]= f[fila][:columna]+\
                        '1'+f[fila][columna+2:]
                return fila*len(f[fila])+columna+2
        return None

def izquierda(f,fila,columna):
        if columna-1<0: return None
        if f[fila][columna-1]=='y':
                f[fila]= f[fila][:columna-2]+\
                        '1'+f[fila][columna:]
                return -2
        if f[fila][columna-1]=='0':
                f[fila]= f[fila][:columna-2]+\
                        '1'+f[fila][columna:]
                return fila*len(f[fila])+columna+1
        return None

def crearLaberinto(a,b):
	#[x.apend() for x in [] ]
	return [range(a) for i in range(b)]
	#return choice(["escribe","algo"])

def crearRecorrido():
	print ( "creando recorrido ")
	return False


def encontrarX(f):
	for fila in range(len(f)):
		for columna in range(len(f[0])):
			if f[fila][columna]=='x':return [fila,columna]

with open("laberinto.txt","r") as f:
	print  "Laberinto: "
	print (f.read())
	f.seek(0)
	laberinto=f.readlines()
	posiciones = encontrarX(laberinto)
	arbol=Nodo(-1,[])
	print (recorrer(laberinto,arbol,posiciones[0],posiciones[1]) )
