
p_list([], [], [], []).
p_list(Xs, Active, Unactive, Res) :-
    select(X, Active, N_Active),
    p_list(Xs, Unactive, N_Active, N_Res),
    Res = [X | N_Res].

p_list([X | Xs], Active, Unactive, Res) :-
    p_list(Xs, [X | Unactive], Active, N_Res),
    Res = [X | N_Res].

lista(N, L) :-
    numlist(1, N, L1),
    p_list(L1,[],[],L).


% partial_list(0,[],[],[]).
% partial_list(N,[N|L1],[N|L2],L3) :-
%     N > 0,
%     M is N-1,
%     partial_list(M,L1,L3,L2).
% partial_list(N,[X|L1],L2,L3) :-
%     N > 0,
%     between(1,N,X),
%     \+ member(X,L2),
%     \+ member(X,L3),
%     sort(0,@>,[X|L3],L4),
%     partial_list(N,L1,L4,L2).

% lista(N,L) :- N > 0, partial_list(N,L2,[],[]), reverse(L,L2).
