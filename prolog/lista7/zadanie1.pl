% zadanie 1

merge(X, L2, R) :- freeze(L2, (L2 = [], freeze(X, R = X))).
merge(L1, X, R) :- freeze(L1, (L1 = [], freeze(X, R = X))).
merge([X | L1], [Y| L2], R):-
    freeze(X,
        freeze(Y,
            (X > Y -> 
                (R = [Y|L3], merge([X|L1], L2, L3));
                (R = [X|L3], merge(L1, [Y|L2], L3))
            )
        )
    ), !.
