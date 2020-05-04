:- ['../lista5/zadanie1'].
:- ['zadanie1'].

replace([], ID, N, [ID = N]).
replace([ID = _ | AS], ID, N, [ID = N | AS]) :- !.
replace([ID1 = W1 | AS1], ID, N, [ID1 = W1 | AS2]) :- replace(AS1, ID, N, AS2).

get([ID = N | _], ID, N) :- !.
get([_ | AS], ID, N) :- get(AS, ID, N).

value(int(N), _, N).
value(id(ID), AS, N) :- get(AS, ID, N).
value(W1 + W2, AS, N) :-
  value(W1, AS, N1),
  value(W2, AS, N2), N is N1 + N2.
value(W1 - W2, AS, N) :-
  value(W1, AS, N1),
  value(W2, AS, N2),
  N is N1 - N2.
value(W1 * W2, AS, N) :-
  value(W1, AS, N1),
  value(W2, AS, N2),
  N is N1 * N2.
value(W1 / W2, AS, N) :-
  value(W1, AS, N1),
  value(W2, AS, N2),
  N2 =\= 0,
  N is N1 div N2.
value(W1 mod W2, AS, N) :-
  value(W1, AS, N1),
  value(W2, AS, N2),
  N2 =\= 0,
  N is N1 mod N2.

tru(W1 =:= W2, AS) :-
  value(W1, AS, N1),
  value(W2, AS, N2),
  N1 =:= N2.
tru(W1 =\= W2, AS) :-
  value(W1, AS, N1),
  value(W2, AS, N2),
  N1 =\= N2.
tru(W1 < W2, AS) :-
  value(W1, AS, N1),
  value(W2, AS, N2),
  N1 < N2.
tru(W1 > W2, AS) :-
  value(W1, AS, N1),
  value(W2, AS, N2),
  N1 > N2.
tru(W1 >= W2, AS) :-
  value(W1, AS, N1),
  value(W2, AS, N2),
  N1 >= N2.
tru(W1 =< W2, AS) :-
  value(W1, AS, N1),
  value(W2, AS, N2),
  N1 =< N2.
tru((W1, W2), AS) :-
  tru(W1, AS),
  tru(W2, AS).
tru((W1; W2), AS) :-
  ( tru(W1, AS), !;
    tru(W2, AS)).

interpr([], _).
interpr([read(ID) | PGM], AS) :-
  !, read(N),
  integer(N),
  replace(AS, ID, N, AS1),
  interpr(PGM, AS1).
interpr([write(W) | PGM], AS) :-
  !, value(W, AS, WART),
  write(WART), nl,
  interpr(PGM, AS).
interpr([assign(ID, W) | PGM], AS) :-
  !, value(W, AS, WAR),
  replace(AS, ID, WAR, AS1),
  interpr(PGM, AS1).
interpr([if(C, P) | PGM], ASO) :- !, interpr([if(C, P, []) | PGM], ASO).
interpr([if(C, P1, P2) | PGM], AS) :-
    !, (tru(C, AS) ->
          append(P1, PGM, DALEJ);
          append(P2, PGM, DALEJ)),
    interpr(DALEJ, AS).
interpr([while(C, P) | PGM], AS) :-
  !, append(P, [while(C, P)], DALEJ),
  interpr([if(C, DALEJ) | PGM], AS).

interpr(PROGRAM) :- interpr(PROGRAM, []).

wykonaj(F) :-
    open(F, read, S),
    scanner(S, T),
    close(S),
    phrase(program(P), T),
    interpr(P).
