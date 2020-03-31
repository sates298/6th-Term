% zadanie 2
jednokrotnie(X, L) :-
    select(X, L, L1),
    \+ member(X, L1).
    
dwkrotnie(X, L) :-
    select(X, L, L1),
    select(X, L1, L2),
    \+ member(X, L2).