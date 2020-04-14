program --> [ ]; instruction, [;], program.

instruction --> ident ,[:=], expression.
instruction --> [read], ident.
instruction --> [write], expression.
instruction --> [if], condition, [then], program, [fi].
instruction --> [if], condition, [then], program, [else], program, [fi].
instruction --> [while], condition, [do], program, [od].

expression --> ingredient, [+], expression.
expression --> ingredient, [-], expression.
expression --> ingredient.

ingredient --> factor, [*], ingredient.
ingredient --> factor, [/], ingredient.
ingredient --> factor, [mod], ingredient.
ingredient --> factor.

factor --> ident.
factor --> natural.
factor --> ['('], expression, [')'].

condition --> conjuction, [or], condition.
condition --> conjuction.

conjuction --> simple, [and], conjuction.
conjuction --> simple.

simple --> expression, [=], expression.
simple --> expression, [/=], expression.
simple --> expression, [<], expression.
simple --> expression, [>], expression.
simple --> expression, [>=], expression.
simple --> expression, [=<], expression.
simple --> ['('], condition, [')'].
