s --> np, vp.                /* sentence */

np --> pn.                   /* noun phrase */
np --> d, n, rel.

vp --> tv, np.               /* verb phrase */
vp --> iv.

rel --> [].                  /*  relative clause */
rel --> rpn, vp.

pn --> [PN], {pn(PN)}.       /* proper noun */
pn(mary).
pn(henry).

rpn --> [RPN], {rpn(RPN)}.   /* relative pronoun */
rpn(that).
rpn(which).
rpn(who).

iv --> [IV], {iv(IV)}.       /*  intransitive verb */
iv(runs).
iv(sits).

d --> [DET], {d(DET)}.       /* determiner */
d(a).
d(the).

n --> [N], {n(N)}.           /* noun */
n(book).
n(girl).
n(boy).

tv --> [TV], {tv(TV)}.       /* transitive verb */
tv(gives).
tv(reads).