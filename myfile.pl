sentence(NP, VP) --> noun_phrase(NP), verb_phrase(VP).
noun_phrase(np(Noun, Adj)) --> det, adjectives(Adj), noun(Noun).

det --> [D], { det(D) }.
det --> [].

noun(N) --> [N], { noun(N) }.

adjectives([]) --> [].
adjectives([A|As]) --> adjective(A), adjectives(As).
adjective(A) --> [A], { adj(A) }.

verb_phrase(vp(Verb, Noun)) --> verb(Verb), noun_phrase(Noun).

verb(V) --> [V], { verb(V) }.