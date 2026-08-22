 
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
emission_count = {}

for sentence in corpus:
    for word, tag in sentence:
        tag_count[tag] = tag_count.get(tag, 0) + 1
        emission_count[(tag, word)] = emission_count.get((tag, word), 0) + 1

print("Emission Probabilities\n")

for key in emission_count:
    tag, word = key
    probability = emission_count[key] / tag_count[tag]
    print(f"P({word}|{tag}) = {probability:.3f}")
