grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"], ["a"]],
    "N": [["cat"], ["dog"], ["milk"]],
    "V": [["drinks"], ["eats"]]
}

sentence = input("Enter sentence: ").lower().split()

def parse(symbol, words, position):
    if symbol not in grammar:
        if position < len(words) and symbol == words[position]:
            return position + 1
        return None

    for rule in grammar[symbol]:
        pos = position
        success = True
        for item in rule:
            pos = parse(item, words, pos)
            if pos is None:
                success = False
                break
        if success:
            return pos

    return None

result = parse("S", sentence, 0)

if result == len(sentence):
    print("Sentence accepted")
else:
    print("Sentence rejected")
