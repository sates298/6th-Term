% 1 zadanie
ojciec(w, e).
ojciec(a, m).
ojciec(m, s).
ojciec(m, g).
matka(e, s).
matka(e, g).
matka(b, e).
matka(ma, m).
mezczyzna(w).
mezczyzna(m).
mezczyzna(g).
kobieta(e).
kobieta(g).
kobieta(ma).
kobieta(b).
rodzic(X, Y) :-
    (   matka(X, Y)
    ;   ojciec(X, Y)
    ).
diff(X, Y) :-
    X\=Y.

jest_matka(X) :-
    matka(X, _).
jest_ojcem(X) :-
    ojciec(X, _).
jest_synem(X) :-
    mezczyzna(X),
    rodzic(_, X).
rodzenstwo(X, Y) :-
    diff(X, Y),
    rodzic(Z, X),
    rodzic(Z, Y).
siostra(X, Y) :-
    kobieta(X),
    rodzenstwo(X, Y).
dziadek(X, Y) :-
    ojciec(X, Z),
    rodzic(Z, Y).

% 2 zadanie
on(second, first).
on(third, second).
on(fourth, third).
on(fifth, fourth).

above_stack(Block1, Block2) :-
    on(Block1, Block2);
    on(Block3, Block2),above_stack(Block1, Block3).

% 3 zadanie 
left_of(pencil, hourglass).
left_of(hourglass, butterfly).
left_of(butterfly, fish).
above(bicycle, pencil).
above(camera, butterfly).

right_of(Object1, Object2) :-
    left_of(Object2, Object1).
below(Object1, Object2) :-
    above(Object2, Object1).
on_left(Object1, Object2) :-
    (   left_of(Object1, Object2)
    ;   left_of(Object1, Object3),
        on_left(Object3, Object2)
    ).
on_right(Object1, Object2) :-
    (   right_of(Object1, Object2)
    ;   right_of(Object1, Object3),
        on_right(Object3, Object2)
    ).
on_above(Object1, Object2) :-
    (   above(Object1, Object2)
    ;   above(Object1, Object3),
        on_above(Object3, Object2)
    ).
higher(Object1, Object2) :-
    (   on_above(Object1, Object2)
    ;   on_left(Object3, Object2),
        on_above(Object1, Object3)
    ;   on_right(Object3, Object2),
        on_above(Object1, Object3)
    ). 
% 4 zadanie
% le(a, b).
% le(a, a).
% le(a, c).
% le(a, d).
% le(b, b).
% le(b, c).
% le(b, d).
% le(c, d).
% le(c, c).
% le(d, d).
maksymalny(X) :-
    \+ ( le(X, Y),
         X\=Y
       ),
    le(_, X),
    !.

minimalny(X) :-
    \+ ( le(Y, X),
         X\=Y
       ),
    le(X, _),
    !.

najwiekszy(X) :-
    \+ ( le(_, Y),
         \+ le(Y, X)
       ).

najmniejszy(X) :-
    \+ ( le(Y, _),
         \+ le(X, Y)
       ).
le(1,1).
le(1,2).
le(1,3).
le(1,4).
le(1,5).
le(1,6).

le(2,1).
le(2,2).
le(2,3).
le(2,4).
le(2,5).
le(2,6).

le(4,1).
le(4,2).
le(4,3).
le(4,4).
le(4,7).

le(5,1).
le(5,2).
le(5,3).
le(5,7).
le(5,5).
le(5,6).

le(6,1).
le(6,2).
le(6,3).
le(6,5).
le(6,6).
le(6,7).

le(3,1).
le(3,2).
le(3,3).
le(3,4).
le(3,5).
le(3,6).
le(3,7).

le(7,3).
le(7,4).
le(7,5).
le(7,6).
le(7,7).
% 5 zadanie
nczesciowy_porzadek :-
    le(X, Y),
    (   (   \+ le(X, X)
        ;   \+ le(Y, Y)
        )
    ;   le(Y, Z),
        \+ le(X, Z)
    ;   le(Y, X),
        X\=Y
    ).

czesciowy_porzadek :-
    \+ nczesciowy_porzadek.

% % 6 zadanie
is_divisable(X, Y) :-
    0 is X mod Y,
    !.
is_divisable(X, Y) :-
    X>Y+1,
    is_divisable(X, Y+1). 

is_prime(2).
is_prime(X) :-
    X<2,
    !,
    false.
is_prime(X) :-
    \+ is_divisable(X, 2).
prime(LO, HI, X) :-
    between(LO, HI, X),
    is_prime(X). 