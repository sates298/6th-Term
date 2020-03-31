% zadanie 2
left(L, R, H) :- append(_, [L,R|_], H).
neighbour(N, T, H) :- left(N,T,H) ; left(T, N, H).

% who, color, drink, smoke, animal
riddle(X) :-
    H = [H1, _, H3, _, _],
    H1 = [norwegian, _, _, _, _],
    member([englishman,red,_,_,_], H),
    left([_,green,_,_,_], [_,white,_,_,_], H),
    member([dane,_,tea,_,_], H),
    neighbour([_,_,_,light,_], [_,_,_,_,cats], H),
    member([_,yellow,_,cigar,_], H),
    member([niemiec,_,_,pipe,_], H),
    H3 = [_,_,milk,_,_],
    neighbour([_,_,_,light,_], [_,_,water,_,_], H),
    member([_,_,_,without_filter,birds], H),
    member([swede,_,_,_,dogs], H),
    neighbour([norwegian,_,_,_,_], [_,blue,_,_,_], H),
    neighbour([_,yellow,_,_,_], [_,_,_,_,horses], H),
    member([_,_,beer,menthol,_], H),
    member([_,green,coffee,_,_], H),
    member([X,_,_,_,fishes], H).

rybki(X) :- riddle(X), !.
