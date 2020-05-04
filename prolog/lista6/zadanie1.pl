:- ['../lista5/zadanie1'].

program([]) --> [].
program([I | P]) --> instruction(I), [sep(;)], program(P).

instruction(assign(ID, EX)) --> [id(ID)], [sep(:=)], expression(EX).
instruction(read(ID)) --> [key(read)], [id(ID)].
instruction(write(EXPR)) --> [key(write)], expression(EXPR).
instruction(if(CND, PRG)) --> [key(if)], condition(CND), [key(then)], program(PRG), [key(fi)].
instruction(if(CND, PRG, ELS)) --> [key(if)], condition(CND), [key(then)], program(PRG),
    [key(else)], program(ELS), [key(fi)].
instruction(while(CND, PRG)) --> [key(while)], condition(CND), [key(do)], program(PRG), [key(od)].

expression(C + E) --> ingredient(C), [sep(+)], expression(E).
expression(C - E) --> ingredient(C), [sep(-)], expression(E).
expression(C) --> ingredient(C).

ingredient(E * C) --> factor(E), [sep(*)], ingredient(C).
ingredient(E / C) --> factor(E), [sep(/)], ingredient(C).
ingredient(E mod C) --> factor(E), [key(mod)], ingredient(C).
ingredient(E) --> factor(E).

factor(id(E)) --> [id(E)].
factor(int(E)) --> [int(E)].
factor(E) --> [sep('(')], expression(E), [sep(')')].

condition(C1; C2) --> conjunction(C1), [key(or)], condition(C2).
condition(C) --> conjunction(C).

conjunction(S ',' C) --> simple(S), [key(and)], conjunction(C).
conjunction(S) --> simple(S).

simple(E1 =:= E2) --> expression(E1), [sep(=)], expression(E2).
simple(E1 =\= E2) --> expression(E1), [sep(/=)], expression(E2).
simple(E1 < E2) --> expression(E1), [sep(<)], expression(E2).
simple(E1 > E2) --> expression(E1), [sep(>)], expression(E2).
simple(E1 >= E2) --> expression(E1), [sep(>=)], expression(E2).
simple(E1 =< E2) --> expression(E1), [sep(<=)], expression(E2).
simple(C) --> [sep('(')], condition(C), [sep(')')].
