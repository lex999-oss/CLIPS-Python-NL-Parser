import nltk
import clips
import string

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# input text from file or taken from user input

# from file
f = open("text.txt", "r")
text = f.read()
text = text.translate(str.maketrans('', '', string.punctuation))
print(text)

# user input
# print("Please introduce a sentence or text you want to proccess : ")
# sentence = input()
# print("Your given input is : ", sentence)

tokens = nltk.word_tokenize(text)
tagged = nltk.pos_tag(tokens)

print(tagged)

to_parse = ""
for t in tagged:
    to_parse += t[1]
    to_parse += " "

environment = clips.Environment()

# # assert a new fact through its template
# fact = environment.assert_string('(sentence ' + to_parse + ')')
#
# print(fact.asserted)
#
# # execute the activations in the agenda
# environment.run()

deffacts = """
(deffacts facts
        (waiting_input)
        (answer)
        (rule G1 S NN  A)
        (rule G2 A VBD EPS)
        (rule G3 A NN C)
        (rule G4 C VBD EPS)
        )
        """
#         (rule G2  A librarie B)
#         (rule G3  B am C)
#         (rule G4  C cumparat D)
#         (rule G5  D o E)
# 		(rule G6  E carte EPS)
# 		(rule G7  S Am G)
# 		(rule G8  G citit H)
# 		(rule G9  H o E)
# 		(rule G10  H la I)
# 		(rule G11  I librarie EPS)
# 		(rule G12  G cumparat J)
# 		(rule G13  J si K)
# 		(rule G14  K am C)
# 		(rule G15  C citit H)
# )
# """
read_input = """
(defrule read_input
        ?a <- (waiting_input)
        =>
        (printout t "Insert sentence: " crlf)
        (assert (text S (explode$ (readline))))

        (retract ?a)
)
"""

apply_rule = """
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
"""
succes = """
(defrule success
        ?a <- (text EPS)
        (answer $?steps)
        =>
        (printout t "YES" $?steps crlf)

        (retract ?a)
)
"""

failure = """
(defrule failure
        ?a <- (text $?)
        =>
        (printout t "NO" crlf)

        (retract ?a)
)
"""
environment.clear()
environment.build(deffacts)
environment.build(read_input)
environment.build(apply_rule)
environment.build(failure)
environment.build(succes)
environment.reset()
environment.run()
