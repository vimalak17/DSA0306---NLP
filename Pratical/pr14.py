grammar = {
    "S": [["NP_SINGULAR", "VP_SINGULAR"], ["NP_PLURAL", "VP_PLURAL"]],
    "NP_SINGULAR": [["Det", "N_SINGULAR"]],
    "NP_PLURAL": [["Det", "N_PLURAL"]],
    "VP_SINGULAR": [["V_SINGULAR"]],
    "VP_PLURAL": [["V_PLURAL"]],
    "Det": [["the"], ["a"]],
    "N_SINGULAR": [["boy"], ["girl"], ["cat"]],
    "N_PLURAL": [["boys"], ["girls"], ["cats"]],
    "V_SINGULAR": [["runs"], ["eats"], ["drinks"]],
    "V_PLURAL": [["run"], ["eat"], ["drink"]]
}

sentence = input("Enter sentence: ").lower().split()

def parse(symbol, words, position):
    if symbol not in grammar:
        if position < len(words) and symbol == words[position]:
            return position + 1
        return None

    for rule in grammar[symbol]:
        pos = position
        valid = True

        for item in rule:
            pos = parse(item, words, pos)

            if pos is None:
                valid = False
                break

        if valid:
            return pos

    return None

result = parse("S", sentence, 0)

if result == len(sentence):
    print("Subject-Verb agreement is correct")
else:
    print("Subject-Verb agreement is incorrect")
