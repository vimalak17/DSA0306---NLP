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
            return position + 1, symbol
        return None, None

    for rule in grammar[symbol]:
        pos = position
        children = []
        valid = True

        for item in rule:
            new_pos, tree = parse(item, words, pos)

            if new_pos is None:
                valid = False
                break

            pos = new_pos
            children.append(tree)

        if valid:
            return pos, (symbol, children)

    return None, None

def print_tree(tree, level=0):
    if isinstance(tree, str):
        print("  " * level + tree)
        return

    symbol, children = tree
    print("  " * level + symbol)

    for child in children:
        print_tree(child, level + 1)

position, tree = parse("S", sentence, 0)

if position == len(sentence):
    print("Parse Tree:")
    print_tree(tree)
else:
    print("Sentence cannot be parsed")
