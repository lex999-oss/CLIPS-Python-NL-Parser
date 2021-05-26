(deffacts facts
        (waiting_input)
        (answer)
        (rule G1  S La A)
        (rule G2  A librarie B)
        (rule G3  B am C)
        (rule G4  C cumparat D)
        (rule G5  D o E)
		(rule G6  E carte EPS)
		(rule G7  S Am G)
		(rule G8  G citit H)
		(rule G9  H o E)
		(rule G10  H la I)
		(rule G11  I librarie EPS)
		(rule G12  G cumparat J)
		(rule G13  J si K)
		(rule G14  K am C)
		(rule G15  C citit H)
		
		
		

		

		

)

(defrule read_input
        ?a <- (waiting_input)
        =>
        (printout t "Insert sentence: " crlf)
        (assert (text S (explode$ (readline))))

        (retract ?a)
)

(defrule apply_rule
        (rule ?g ?nonterminal ?first ?next)
        ?a <- (text ?nonterminal ?first $?rest)
        ?b <- (answer $?steps)
        =>
        (assert (text ?next $?rest))
        (assert (answer $?steps ?g))

        (retract ?a)
        (retract ?b)
)

(defrule success
        ?a <- (text EPS)
        (answer $?steps)
        =>
        (printout t "YES" $?steps crlf)

        (retract ?a)
)

(defrule failure
        ?a <- (text $?)
        =>
        (printout t "NO" crlf)

        (retract ?a)
)
