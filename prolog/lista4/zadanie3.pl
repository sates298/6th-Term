
% +-1-+-2-+-3-+
% 4   5   6   7
% +-8-+-9-+-10-+
% 11  12  13   14
% +-15-+-16-+-17-+
% 18   19   20   21
% +-22-+-23-+-24-+

square(_, 0, []).

square(1, 1, [ 1,  4,  5,  8]).
square(1, 1, [ 2,  5,  6,  9]).
square(1, 1, [ 3,  6,  7, 10]).
square(1, 1, [ 8, 11, 12, 15]).
square(1, 1, [ 9, 12, 13, 16]).
square(1, 1, [10, 13, 14, 17]).
square(1, 1, [15, 18, 19, 22]).
square(1, 1, [16, 19, 20, 23]).
square(1, 1, [17, 20, 21, 24]).

square(2, 1, [ 1,  2,  4,  6, 11, 13, 15, 16]).
square(2, 1, [ 2,  3,  5,  7, 12, 14, 16, 17]).
square(2, 1, [ 8,  9, 11, 13, 18, 20, 22, 23]).
square(2, 1, [ 9, 10, 12, 14, 19, 21, 23, 24]).

square(3, 1, [1, 2, 3, 4, 7, 11, 14, 18, 21, 22, 23, 24]).

square(S, N, R) :-
    N1 is N - 1,
    N1 > 0,
    square(S, 1, X),
    square(S, N1, Y),
    min_list(X, SX),
    min_list(Y, SY),
    SX < SY,
    union(X, Y, R),
    R \= Y.

cond_write(W, L, X) :-
    member(X, L) ->
    write(W), !;
    atom_length(W, N), tab(N).

draw_h(L, N1, N2, N3) :-
    write(+), cond_write(---, L, N1),
    write(+), cond_write(---, L, N2),
    write(+), cond_write(---, L, N3),
    write(+), nl.

draw_v(L, N1, N2, N3, N4) :-
    cond_write("|", L, N1), tab(3),
    cond_write("|", L, N2), tab(3),
    cond_write("|", L, N3), tab(3),
    cond_write("|", L, N4), nl.

draw(L) :-
    write("Rozwiazanie:"), nl,
    draw_h(L, 1, 2, 3),
    draw_v(L, 4, 5, 6, 7),
    draw_h(L, 8, 9, 10),
    draw_v(L, 11, 12, 13, 14),
    draw_h(L, 15, 16, 17),
    draw_v(L, 18, 19, 20, 21),
    draw_h(L, 22, 23, 24).

solution(C, B, M, S) :-
    square(3, B, S3),
    square(2, M, S2),
    square(1, S, S1),
    union(S1, S2, U),
    union(U, S3, R),
    length(R, N),
    C is 24 - N,
    draw(R).

matches(N, (C), _, M, S) :- C = duze(CN), solution(N, CN, M, S).
matches(N, (C), B, _, S) :- C = srednie(CN), solution(N, B, CN, S).
matches(N, (C), B, M, _) :- C = male(CN), solution(N, B, M, CN).


matches(N, (C, Cs), _ , M, S) :- C = duze(CN), matches(N, (Cs), CN, M, S).
matches(N, (C, Cs), B, _, S) :- C = srednie(CN), matches(N, (Cs), B, CN, S).
matches(N, (C, Cs), B, M, _) :- C = male(CN), matches(N, (Cs), B, M, CN).

zapalki(N, C) :- matches(N, C, 0, 0, 0).
