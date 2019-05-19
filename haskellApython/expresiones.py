
#!bin/python2.7

#pag 42
def sumar(x):
	if x==[]: return 0
	return x[0] + sumar(x[1:])

#pag 44
def igualar(x,y):
	if y!=x:
		return False
	else:
		return True

#pag 46
def ubicacion(x,n):
	return x[n]

#pag 48
def pares(x):
	if x==[]: return 0 
	if x[0]%2 ==0: return 1 + pares(x[1:])
	return pares(x[1:])

#pag 50
def primo(x):
	if len(divisores(x)) <= 2: return True
	else: return False

def divisores(x):
	return  [ [a] for a in range(1,x+1) if x%a == 0  ]
