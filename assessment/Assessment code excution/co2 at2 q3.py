 

corpus = [
    [("The","DT"),("boy","NN"),("eats","VBZ"),("rice","NN")],
    [("The","DT"),("girl","NN"),("drinks","VBZ"),("milk","NN")],
    [("A","DT"),("cat","NN"),("drinks","VBZ"),("milk","NN")],
    [("The","DT"),("dog","NN"),("chases","VBZ"),("cat","NN")],
    [("A","DT"),("teacher","NN"),("teaches","VBZ"),("students","NNS")],
    [("Students","NNS"),("study","VBP"),("English","NN")],
    [("Birds","NNS"),("fly","VBP"),("high","RB")],
    [("Children","NNS"),("play","VBP"),("games","NNS")]
]

tag_count = {}
transition_count = {}

for sentence in corpus:

    previous = None

    for word, tag in sentence:

        tag_count[tag] = tag_count.get(tag, 0) + 1

        if previous is not None:
            transition_count[(previous, tag)] = transition_count.get((previous, tag), 0) + 1

        previous = tag

print("Transition Probabilities\n")

for key in transition_count:

    previous, current = key

    probability = transition_count[key] / tag_count[previous]

    print(f"P({current}|{previous}) = {probability:.3f}")
