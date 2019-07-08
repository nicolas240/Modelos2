padrede('','nicolas').
padrede('japi','alberto').
padrede('ales','alberto').
padrede('niao','japi').
padrede('ales','camilo').
padrede('camilo','francisco').
padrede('jose','marlon').


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
