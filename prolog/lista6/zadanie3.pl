% wywołanie s1(`aabb`, ``)
s1 --> `a`, x, `b`.
s1 --> x.
x --> `ab`.
x --> ``.

% wywołanie s2(`aabbcc`, ``)
s2 --> a(N), b(N), c(N).
a(0) --> ``.
a(M) --> `a`, a(N), {M is N + 1}.
b(0) --> ``.
b(M) --> `b`, b(N), {M is N + 1}.
c(0) --> ``.
c(M) --> `c`, c(N), {M is N + 1}.

% wywołanie s3([a,....,b],[]).
s3 --> symbolsN(Sem, a), symbolsFib(Sem, b).
symbolsN(end, _) --> [].
symbolsN(s(Sem), S) --> [S], symbolsN(Sem, S).
symbolsFib(end, _) --> [].
symbolsFib(s(end), S) --> [S].
symbolsFib(s(s(Sem)), S) --> symbolsFib(s(Sem), S), symbolsFib(Sem, S).


p([]) --> [].
p([X | Xs]) --> [X], p(Xs).
