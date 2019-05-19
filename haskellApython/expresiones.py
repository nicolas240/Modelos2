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
	result=0 
	for a in x:
		if a%2 ==0: result+=1
	return result

#pag 50
def primo(x):
	cont=0
	for a in range(1,x):
		if x%a == 0:
			cont+=1
		if cont > 2:
			return False
	return True
