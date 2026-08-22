 
sentence = "The cat drinks milk"

words = sentence.split()
 
pos_dictionary = {
    "The": "DT",
    "A": "DT",
    "boy": "NN",
    "girl": "NN",
    "cat": "NN",
    "dog": "NN",
    "teacher": "NN",
    "rice": "NN",
    "milk": "NN",
    "English": "NN",
    "eats": "VBZ",
    "drinks": "VBZ",
    "chases": "VBZ",
    "teaches": "VBZ",
    "Students": "NNS",
    "Birds": "NNS",
    "Children": "NNS",
    "students": "NNS",
    "games": "NNS",
    "study": "VBP",
    "fly": "VBP",
    "play": "VBP",
    "high": "RB"
}

print("Input Sentence:")
print(sentence)

print("\nPredicted POS Tags:")

predicted_tags = []

for word in words:
    tag = pos_dictionary.get(word, "NN")    
    predicted_tags.append(tag)
    print(word, "->", tag)

print("\nPOS Tag Sequence:")
print(" ".join(predicted_tags))
