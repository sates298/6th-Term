norm(X,Y,N) :-
    number(X),
    number(Y),
    Z is X-Y,
    N is Z*Z.

s_norms([X], A, S, R) :- norm(X, A, N), R is N+S.
s_norms([X|L], A, S, R) :-
    norm(X,A,N),
    s_norms(L, A, S+N, R), !.

wariancja(L, R) :- 
    sumlist(L,S),
    length(L, Lgth),
    (Lgth > 0 -> A is S/Lgth; A is 0), 
    s_norms(L,A,0,RR),
    R is RR/Lgth.
