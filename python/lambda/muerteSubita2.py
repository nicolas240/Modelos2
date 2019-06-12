#!bin/python2.7

from functools import reduce

def superPar(x):
	if x=='': return True
	if int(x[0])%2!=0: return False
	return True and superPar(x[1:])

""" 1-) lista de primer y ultimo elemento  de una lista de listas"""
l=[[22,11,32],[10,20,44,33]]
print '1-)',l
print  map( lambda x:  [x[0],x[len(x)-1]],l)


""" 2-) Lista de numeros super pares"""
l=[22,11,32,10,20,44,33]
print '2-)',l
print  filter( lambda y: superPar(str(y)),l)
#print  filter( lambda y: map(int,str(y))[0]%2==0 and map(int,str(y))[1]%2==0 ,l)

""" 3-) Valores maximos de una lista de listas"""

l=[[22,11,32],[10,20,44,33]]
print '3-)',l
print  map( lambda x: reduce(lambda y,z: y if y>z else z  ,x ),l)

""" 4-) Valores minimos de cada lista de una lista de listas que cumplen con numero superpar """
l=[[222,103,224,235],[10,20,44,33]]
print '4-)',l
print  map( lambda x: reduce( lambda y,z: y if y<z else z, filter(lambda w: superPar(str(w)),x ) ) ,l)

"""5-) De una lista los valores menores a la potencia de 5 de la cabeza de la lista """
l=[2,3,10,32,33]
print '5-)',l
print filter(lambda x: x<pow(l[0],5),l)


"""6-) Tuplas (x,y) tal que x sea el numero triangular de y"""
t=(55,10)
print '6-)',t
print filter(lambda z: z==reduce(lambda x,y: x+y  ,range(t[1]+1)),t[:len(t)] )
