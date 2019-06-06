#!bin/python2.7

import functools

def recorrer(f,arbol, posicion):
                #arriba(f,len(f.readline()))
                """Un if para mirar si hay dos raices o dos puntos de llegada """
                if(len(filter(lambda x: x=='x',functools.reduce(lambda x,y: x+y, f) ))!=1 or len(filter(lambda x: x=='y', functools.reduce(lambda x,y: x+y, f) ))!=1):
                        return False
                """hacer un if de si el valor de vacio es (nose digamos que -2) no se recorra"""
		print ("Arriba",arriba(f,posicion[0],posicion[1]))
                print ("Abajo",abajo(f,posicion[0],posicion[1]))
                print ("Derecha",derecha(f,posicion[0],posicion[1]))
                print ("Izquierda",izquierda(f,posicion[0],posicion[1]))
		
                #print (functools.reduce(lambda x,y: x+y[4],f ) )
                #print( l for l in f[0] if l=="1")
                #f.seek(posicion+1)
                #f.write("b")
                #print (f.read(1))
                return True

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
        if fila+1>len(f): return None
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
        if columna+1>len(f[fila]): return None
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
	laberinto = f.readlines()
	print (recorrer(laberinto,14,encontrarX(laberinto)) )
