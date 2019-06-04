#!bin/python2.7

print  "Laberinto"

for line in open("laberinto.txt","r").readlines(): print line.split()

def recorrerLaberinto():
	if path.isfile("laberinto.txt"):
		return crearRecorrido()
	open("laberinto.txt", 'w').writelines(crearLaberinto(randrange(10),randrange(10)))
	return crearRecorrido()

def crearLaberinto(a,b):
	#[x.apend() for x in [] ]
	return [range(a) for i in range(b)]
	#return choice(["escribe","algo"])

def crearRecorrido():
	print ( "creando recorrido ")
	return False
	
print(recorrerLaberinto())
