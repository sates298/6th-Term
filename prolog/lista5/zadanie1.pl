keyword(read).
keyword(write).
keyword(if).
keyword(then).
keyword(else).
keyword(fi).
keyword(while).
keyword(do).
keyword(od).
keyword(and).
keyword(or).
keyword(mod).

scanner(S, R) :-
  get_char(S, C),
  execute(S, C, R).


execute(S, C, R) :-
  char_type(C, space),
  get_char(S, C1),
  execute(S, C1, R), !.
execute(S, C, R) :-
  char_type(C, lower),
  handle_key(S, C, [], R), !.
execute(S, C, R) :-
  char_type(C, upper),
  handle_id(S, C, [], R), !.
execute(S, C, R) :-
  char_type(C, digit),
  handle_num(S, C, 0, R), !.

execute(S, ;, R) :- one_char(S, ;, R).
execute(S, +, R) :- one_char(S, +, R).
execute(S, -, R) :- one_char(S, -, R).
execute(S, *, R) :- one_char(S, *, R).
execute(S, >, R) :- one_char(S, >, R).
execute(S, '(', R) :- one_char(S, '(', R).
execute(S, ')', R) :- one_char(S, ')', R).

execute(S, /, R) :- two_chars(S, /, =, /=, R).
execute(S, <, R) :- two_chars(S, <, =, <=, R).
execute(S, =, R) :- two_chars(S, =, >, =>, R).
execute(S, :, R) :-
  get_char(S, =),
  get_char(S, C1),
  execute(S, C1, L),
  R = [ sep(:=) | L],
  !.

execute(_, end_of_file, []) :- !.

one_char(S, C, R) :-
  get_char(S, C1),
  execute(S, C1, L),
  R = [ sep(C) | L], !.


two_chars(S, Left, Right, Full, R) :-
  get_char(S, C),
  (C = Right ->
    get_char(S, C1),
    execute(S, C1, L),
    R = [ sep(Full) | L], !
    ;
    execute(S, C, L),
    R = [ sep(Left) | L ], !
  ).


handle_key(S, C, Cs, R) :-
  get_char(S, C1),
  (
     char_type(C1, lower),
     handle_key(S, C1, [ C | Cs ], R);
     reverse([ C | Cs ], KR),
     atom_codes(K, KR),
     keyword(K),
     execute(S, C1, L),
     R = [ key(K) | L]
  ), !.


handle_id(S, C, Cs, R) :-
  get_char(S, C1),
  (
    char_type(C1, upper),
    handle_id(S, C1, [ C | Cs ], R);
    reverse([ C | Cs ], IR),
    atom_codes(I, IR),
    execute(S, C1, L),
    R = [ id(I) | L ]
  ), !.


handle_num(S, C, Ns, R) :-
  char_type(C, digit(CN)),
  N is  Ns * 10 + CN,
  get_char(S, C1),
  (
    char_type(C1, digit),
    handle_num,(S, C1, N, R);
    execute(S, C1, L),
    R = [ int(N) | L ]
  ), !.
