--pag42
sumar:: [Int]->Int
sumar [] = 0
sumar (x:xs) = x +sumar(xs)

--pag43
invertir::Ord a=>[a]->[a]
invertir [] = []
invertir (x:xs) = (invertir xs )++[x]

--pag 44
igualLista:: Eq a => [a]->[a]->Bool
igualLista l1 l2 = l1 == l2

--pag 45
listaOrdenada:: Ord a=>[a]->Bool
listaOrdenada []=True
listaOrdenada [_]=True
listaOrdenada (x:y:xs) = (x<=y) && listaOrdenada(y:xs) 

--pag 46
mostrarUbicacion:: Ord a=>[a]->Int->a
mostrarUbicacion l n = l!!n

--pag 47
mayor::[Int]->Int
mayor (x:xs)
 | x > mayor(xs) = x
 | otherwise = mayor(xs)

--pag 48
contarPares:: [Int]->Int
contarPares []=0
contarPares lista= length [ x | x<- lista, mod x 2 ==0]

--pag 49
cuadrados::[Int]->[Int]
cuadrados [ ] = [ ]
cuadrados l = [x*x | x <-l]

--pag 50

divisible::Int->Int->Bool
divisible x y = (mod x y ) ==0

divisibles::Int->[Int]
divisibles x = [y | y <-[1..x], divisible x y]

esPrimo::Int->Bool
esPrimo n = length (divisibles n) <=2
