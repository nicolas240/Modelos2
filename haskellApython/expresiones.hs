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
mayor :: [Int]->Int
mayor (x:xs)
   | x > mayor(xs) = x
   | otherwise = mayor(xs)
