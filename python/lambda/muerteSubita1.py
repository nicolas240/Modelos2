# -*- coding: cp1252 -*-
from functools import*

def superPar(x):
	if x=='': return True
	if int(x[0])%2!=0: return False
	return True and superPar(x[1:])

'''1-)Extraer de una lista de listas el primer y ultimo elemento de cada lista (0.5 pts)'''

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
lista2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lista3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
listaListas = [lista, lista2, lista3]

print "1-)"
print listaListas
print map(lambda x: [x[0],x[len(x)-1]], listaListas),'\n'

'''2-)Dada una lista de numeros enteros retornar una lista con los numeros superpares
(aquellos cuyos todos sus dígitos son pares) (0.5 pts)'''

lista = [234, 864, 34, 26, 152, 35]
print "2-)"
print lista
print  filter( lambda y: superPar(str(y)),lista),'\n'
#print filter(lambda x:x%2==0, filter(lambda x:(x/10)%2==0 and (x/100)%2==0, lista)),'\n'


'''3-)Extraer los valores máximos de cada lista de una lista de listas (0.5 pts)'''
print "3-)"
print listaListas
print map(lambda subLista: reduce(lambda x,y: x if (x>y) else y, subLista), listaListas), '\n'

'''4-)Extraer los valores mínimos de cada lista de una lista de listas que cumplen el concepto de número superpar (0.5 pts)'''
print "4-)"
print listaListas
print  map( lambda x: reduce( lambda y,z: y if y<z else z, filter(lambda w: superPar(str(w)),x ) ) ,listaListas), '\n'

'''5-)Retornar de una lista los valores menores a la potencia 5 de la cabeza de la lista (0.5 pts)'''
print "5-)"
print lista
print filter(lambda x: x<pow(lista[0],5),lista), '\n'

'''6-)Dada una lista de tuplas caracterizada por (int x, int y) sumar los x que cumplan con el criterio de ser el número triangular de y (2 pts)'''
tupla=(55,10)
print "5-)"
print tupla
print filter(lambda z: z==reduce(lambda x,y: x+y  ,range(tupla[1]+1)),tupla[:len(tupla)])

