
max_sum_r([], B, _, B).

max_sum_r([X|L], B, S, R) :-
    Ns is max(0, S+X),
    Nb is max(B, Ns),
    max_sum_r(L, Nb, Ns, R).

max_sum(L, R) :-
    max_sum_r(L, 0, 0, R).
