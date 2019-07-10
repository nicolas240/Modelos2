padrede('','Maria').
padrede('Maria','Alba').
padrede('Maria','Rosa').
padrede('Maria ','Ester').
padrede('Maria','Magda').
padrede('Maria','Luis').
padrede('Alba','Laura').
padrede('Rosa','Marcela').
padrede('Rosa','Hernan').
padrede('Rosa','Eliana').
padrede('Rosa','Hernan').
padrede('Abraham','Marcela').
padrede('Abraham','Hernan').
padrede('Abraham','Eliana').
padrede('Abraham','Hernan').
padrede('Marcela','Juan').
padrede('Belisario','Juan').
padrede('Ester','Diego').
padrede('Ester','Adriana').
padrede('LuisA','Diego').
padrede('LuisA','Adriana').
padrede('Diaego','Ian').
padrede('Rocio','Ian').
padrede('Magda','Jeison').
padrede('Magda','Gabriela').
padrede('Gabriel','Jeison').
padrede('Gabriel','Gabriela').
padrede('Luis','Mayito').
padrede('Luis','Jenny').
padrede('Luis','Karen').
padrede('MariLuz','Mayito').
padrede('MariLuz','Jenny').
padrede('MariLuz','Karen').
padrede('Jenny','Sebastian').
padrede('Jorge','Sebastian').


hijode(A,B) :- padrede(B,A).
abuelode(A,B) :- padrede(A,C),padrede(B,C), A\==B.
hermanode(A,B) :- padrede(C,A),padrede(C,B), A\==B.
tiode(A,B) :- hermanode(A,C),padrede(C,B). %1er=hermanopapa, 2do=hijodelpapa 
sobrinode(A,B) :- tiode(B,A).
primode(A,B):- tiode(C,A),padrede(C,B). %1er=sobrino c, 2do=hijode
nietode(A,B) :- abuelode(B,A).
esposode(A,B) :- padrede(A,C),padrede(B,C).

familiarde(A,B) :- padrede(A,B).
familiarde(A,B) :- hijode(A,B).
familiarde(A,B) :- primode(A,B).
familiarde(A,B) :- tiode(A,B).
familiarde(A,B) :- abuelode(A,B).
familiarde(A,B) :- sobrinode(A,B).
familiarde(A,B) :- nietode(A,B).
familiarde(A,B) :- esposode(A,B).
feliz(A) :- (esposode(A,C)), C\==A.
