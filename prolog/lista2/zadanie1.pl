środkowy([X],X).
środkowy([_|L1], X) :-
    append(L2, [_], L1),
    środkowy(L2, X).
