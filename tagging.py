import nltk
import clips


def validate_sentence_by_rules(set_of_rules, sentence_tags):
    '''
    :param set_of_rules: array of rules defined previously
    :param sentence_tags: the tags for the sentence we want to parse
    :return: 1 if the sentence cannot be matched with the rules, 2 otherwise
    '''
    rule_wrong = '''
    (defrule wrong
        =>
        (printout t "Wrong!" crlf))
    '''
    env = clips.Environment()
    for counter, element in enumerate(set_of_rules):
        rule = '''
        (defrule rule%s
            (sentence %s)
            =>
            (printout t "Correct!" crlf))
        ''' % (str(counter), element)
        env.build(rule)
    env.build(rule_wrong)
    sentence = ''
    for element in sentence_tags:
        sentence += element
        sentence += ' '
    sentence = sentence[:-1]

    # print(sentence)

    fact_string = f'(sentence {sentence})'
    fact = env.assert_string(fact_string)
    template = fact.template

    assert template.implied == True

    validation_result = env.run()
    return validation_result


# main driver program:

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

rules = ["NN" "VBD" "."]
while 1:
    # user input
    sentence = input("Please introduce a sentence or text you want to proccess : ")
    # print("Your given input is : ", sentence)

    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)

    sentence_tags = []
    for t in tagged:
        sentence_tags.append(t[1])
    cons = validate_sentence_by_rules(rules, sentence_tags)
    if cons == 1:
        print("""Sentence = "%s" is not parsable with the current set of rules.""" % sentence)
        add_to_rules = input("Do you want to add this to the set of rules?")
        if add_to_rules == "YES" or add_to_rules == "Yes" or add_to_rules == "yes":
            new_rule = ""
            for elem in sentence_tags:
                new_rule += elem
                new_rule += " "
            new_rule = new_rule.rstrip(new_rule[-1])
            if sentence_tags not in rules:
                rules.append(new_rule)

    else:
        print("""Sentence = "%s" is parsable with the current set of rules.""" % sentence)
    exit = input("Do you want to exit?")
    if exit == "YES" or exit == "Yes" or exit == "yes":
        break
    else:
        continue
