#!bin/python2.7
with open("prueba.txt","r") as f:
	f.seek(3)
	f.seek(9)
	f.seek(13)
	print (f.read(3))


"""def recorrerLaberinto():
        if path.isfile("laberinto.txt"):
                return crearRecorrido()
        open("laberinto.txt", 'w').writelines(crearLaberinto(randrange(10),randrange(10)>
        return crearRecorrido()"""
