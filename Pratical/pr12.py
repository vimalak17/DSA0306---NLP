grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"], ["a"]],
    "N": [["cat"], ["dog"], ["milk"]],
    "V": [["drinks"], ["eats"]]
}

sentence = input("Enter sentence: ").lower().split()

def earley_parse(words):
    n = len(words)
    chart = [[] for _ in range(n + 1)]
    start = ("START", ("S",), 0, 0)
    chart[0].append(start)

    for i in range(n + 1):
        changed = True
        while changed:
            changed = False

            for state in chart[i][:]:
                lhs, rhs, dot, origin = state

                if dot < len(rhs):
                    symbol = rhs[dot]

                    if symbol in grammar:
                        for rule in grammar[symbol]:
                            new_state = (symbol, tuple(rule), 0, i)
                            if new_state not in chart[i]:
                                chart[i].append(new_state)
                                changed = True

                    elif i < n and symbol == words[i]:
                        new_state = (lhs, rhs, dot + 1, origin)
                        if new_state not in chart[i + 1]:
                            chart[i + 1].append(new_state)

                else:
                    for previous in chart[origin]:
                        plhs, prhs, pdot, porigin = previous
                        if pdot < len(prhs) and prhs[pdot] == lhs:
                            new_state = (plhs, prhs, pdot + 1, porigin)
                            if new_state not in chart[i]:
                                chart[i].append(new_state)
                                changed = True

    final_state = ("START", ("S",), 1, 0)
    return final_state in chart[n]

if earley_parse(sentence):
    print("Sentence accepted")
else:
    print("Sentence rejected")
