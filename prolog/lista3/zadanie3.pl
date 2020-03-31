
inversion(L, X, Y) :-
    append(_, [X|R], L),
    member(Y, R),
    X > Y.

inversion_count(L, C) :-
    findall([X,Y], inversion(L, X, Y), R),
    length(R, C).
    
even_permutation(L, X) :-
    lists:perm(L,X),
    inversion_count(X, C),
    0 is C mod 2.    

odd_permutation(L, X) :-
    lists:perm(L,X),
    inversion_count(X, C),
    1 is C mod 2.    