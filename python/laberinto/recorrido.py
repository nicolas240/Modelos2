#!bin/python2.7

import functools

print  "Laberinto: "

print( open("laberinto.txt","r").read())


def recorrer(f,arbol, posicion):
                #arriba(f,len(f.readline()))
                """Un if para mirar si hay dos raices o dos puntos de llegada """
                if(len(filter(lambda x: x=='x',functools.reduce(lambda x,y: x+y, f) ))!=1 or len(filter(lambda x: x=='y', functools.reduce(lambda x,y: x+y, f) ))!=1):
                        return False
                """hacer un if de si el valor de vacio es (nose digamos que -2) no se recorra"""
                print (arriba(f,posicion))
                #print (functools.reduce(lambda x,y: x+y[4],f ) )
                #print( l for l in f[0] if l=="1")
                #f.seek(posicion+1)
                #f.write("b")
                #print (f.read(1))
                return True

def arriba(f, posicion):
        if posicion[0]-1<0: return None
        if f[posicion[0]-1][posicion[1]]=='y':
                f[posicion[0]-1]= f[posicion[0]-1][:posicion[1]-1]+\
                        '1'+f[posicion[0]-1][posicion[1]+1:]
                return 2
        if f[posicion[0]-1][posicion[1]]=='0':
                f[posicion[0]-1]= f[posicion[0]-1][:posicion[1]-1]+\
                        '1'+f[posicion[0]-1][posicion[1]+1:]
                return 1
        return None

def abajo(f,tam):
        if posicion[0]+1>len(f): return None
        if f[posicion[0]+1][posicion[1]]=='y':
                f[posicion[0]+1]=f[posicion[0]+1][:posicion[1]-1]+\
                        '1'+f[posicion[0]+1][posicion[1]+1:]
                return 2
        if f[posicion[0]+1][posicion[1]]=='0':
                f[posicion[0]+1]=f[posicion[0]+1][:posicion[1]-1]+\
                        '1'+f[posicion[0]+1][posicion[1]+1:]
                return 1
        return None

def derecha(f,tam):
        if posicion[1]+1>len(f[0]): return None
        if f[posicion[0]][posicion[1]+1]=='y':
                f[posicion[0]]= f[posicion[0]][:posicion[1]-1]+\
                        '1'+f[posicion[0]][:posicion[1]+2]
                return 2
        if f[posicion[0]][posicion[1]+1]=='0':
                f[posicion[0]]= f[posicion[0]][:posicion[1]-1]+\
                        '1'+f[posicion[0]][:posicion[1]+2]
                return 1
        return None

def izquierda(f,tam):
        if posicion[1]-1<0: return None
        if f[posicion[0]][posicion[1]-1]=='y':
                f[posicion[0]]= f[posicion[0]][:posicion[1]-2]+\
                        '1'+f[posicion[0]][:posicion[1]]
                return 2
        if f[posicion[0]][posicion[1]-1]=='0':
                f[posicion[0]]= f[posicion[0]][:posicion[1]-2]+\
                        '1'+f[posicion[0]][:posicion[1]]
                return 1
        return None

def crearLaberinto(a,b):
	#[x.apend() for x in [] ]
	return [range(a) for i in range(b)]
	#return choice(["escribe","algo"])

def crearRecorrido():
	print ( "creando recorrido ")
	return False

print (recorrer(open("laberinto.txt","r").readlines(),14,[1,4]) )

"""def recorrerLaberinto():
	if path.isfile("laberinto.txt"):
		return crearRecorrido()
	open("laberinto.txt", 'w').writelines(crearLaberinto(randrange(10),randrange(10)))
	return crearRecorrido()"""
