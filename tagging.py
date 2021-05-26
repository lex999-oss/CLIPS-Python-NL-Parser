import nltk
import pyswip
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
prolog = pyswip.Prolog()
prolog.consult('myfile.pl')
for t in tagged:
    to_parse += t[0]
    to_parse += ","
to_parse = to_parse.rstrip(to_parse[-1])
print(bool(list(prolog.query(f'phrase(sentence(NP,VP), [{to_parse}]).'))))
# 1. Update gramatica == reguli sau assert-uti?
# 2. Cum ar arata un parser?