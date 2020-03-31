arc(a,b).
arc(b,a).
arc(b,c).
arc(c,d).

met(L, X, Y) :- 
    arc(X,Y), \+ member(Y, L);
    arc(X, Z), \+ member(Z, L), met([Z|L], Z, Y). 
osiągalny(X, Y) :-
    X = Y;
    met(X,Y,[X]).
