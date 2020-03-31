build_expression(E1, E2, R) :- member(R,[E1*E2,E1+E2,E1-E2]).
build_expression(E1, E2, R) :- V is E2, V =\= 0, R = (E1/E2).

check_solution(E, R, _) :- R = E.
check_solution(E, R, Mem) :-
    R is E,
    \+ member(R, Mem).
check_solution(E, R, Mem) :-
    Float is R*1.0,
    Float is E,
    \+ member(R, Mem).

expression([X], X, X, _).
expression(L, R, E, Mem):-
    append([X|Xs],[Y|Ys], L),
    expression([X|Xs],E1,E1, [E1|Mem]),
    expression([Y|Ys],E2,E2, [E2|Mem]),
    build_expression(E1, E2, E),
    check_solution(E, R, Mem).

wyrażenie(L,V,E) :- expression(L, V, E, []).
