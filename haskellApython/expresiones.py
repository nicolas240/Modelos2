
#!bin/python2.7

#pag 42
def sumar(x):
	if x==[]: return 0
	return x[0] + sumar(x[1:])

#pag 43 - Invertir lista
def invertir(listaNumeros):
    if listaNumeros == []: return listaNumeros
    return listaNumeros[::-1]

#pag 44
def igualar(x,y):
	if y!=x:
		return False
	else:
		return True
	
#pag 45 - Verificar lista ordenada
def listaOrdenada(lista):
    if lista == []: return True
    if len(lista) == 1: return True
    return (lista[0]<=lista [1] and listaOrdenada(lista[1:]))

#pag 46
def ubicacion(x,n):
	return x[n]

#pag 47 - Mayor elemento lista
def maximo(x):
    return mayor(x[0],x[1:])

def mayor(x,y):
    if y==[]: return x
    if x > y[0]: return mayor(x,y[1:])
    else: return mayor(y[0],y[1:])

#pag 48
def pares(x):
	if x==[]: return 0 
	if x[0]%2 ==0: return 1 + pares(x[1:])
	return pares(x[1:])

#pag 49 - Cuadrados de una lista
def cuadrados(lista):
    return [x**2 for x in lista]

#pag 50
def primo(x):
	if len(divisores(x)) <= 2: return True
	else: return False

def divisores(x):
	return  [ [a] for a in range(1,x+1) if x%a == 0  ]
