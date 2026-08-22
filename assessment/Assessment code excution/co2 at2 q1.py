corpus = [
    "The/DT boy/NN eats/VBZ rice/NN",
    "The/DT girl/NN drinks/VBZ milk/NN",
    "A/DT cat/NN drinks/VBZ milk/NN",
    "The/DT dog/NN chases/VBZ cat/NN",
    "A/DT teacher/NN teaches/VBZ students/NNS",
    "Students/NNS study/VBP English/NN",
    "Birds/NNS fly/VBP high/RB",
    "Children/NNS play/VBP games/NNS"
]

for i, sentence in enumerate(corpus, start=1):

    print("Sentence", i)

    words = []
    tags = []

    tokens = sentence.split()

    for token in tokens:
        word, tag = token.split("/")
        words.append(word)
        tags.append(tag)

    print("Words   :", words)
    print("POS Tags:", tags)
    print("-" * 50)
