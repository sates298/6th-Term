
reguła(X,+,Y,Y) :- number(X), X=:=0,!.
reguła(X,+,Y,X) :- number(Y), Y=:=0,!.

reguła(X,-,Y,X) :- number(Y), Y=:=0,!.
reguła(X,-,X,0).

reguła(X,*,_,0) :- number(X), X=:=0,!.
reguła(_,*,X,0) :- number(X), X=:=0,!.
reguła(X,*,Y,Y) :- number(X), X=:=1,!.
reguła(X,*,Y,X) :- number(Y), Y=:=1,!.

reguła(X,/,Y,X) :- number(Y), Y=:=1,!.
reguła(X,/,X,1).
reguła(X,/,_,0) :- number(X), X=:=0,!.
reguła(X,/,Y,R) :- X = R * Y ; X = Y * R.

simplify_one(X, Y) :-
    X = A * B, simplify_one(A, A1), simplify_one(B, B1), reguła(A1, *, B1, Y);
    X = A / B, simplify_one(A, A1), simplify_one(B, B1), reguła(A1, /, B1, Y);
    X = A + B, simplify_one(A, A1), simplify_one(B, B1), reguła(A1, +, B1, Y);
    X = A - B, simplify_one(A, A1), simplify_one(B, B1), reguła(A1, -, B1, Y);
    X = Y.

uprość(X, Y) :- simplify_one(X, Y), !.