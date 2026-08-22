 

sentence = ["The", "cat", "drinks", "milk"]

predicted_tags = []

for word in sentence:

    if word in ["The", "A"]:
        predicted_tags.append("DT")

    elif word in ["boy", "girl", "cat", "dog", "rice", "milk", "English"]:
        predicted_tags.append("NN")

    elif word in ["drinks", "eats", "chases", "teaches"]:
        predicted_tags.append("VBZ")

    elif word in ["students", "games", "Students", "Birds", "Children"]:
        predicted_tags.append("NNS")

    elif word in ["study", "fly", "play"]:
        predicted_tags.append("VBP")

    elif word == "high":
        predicted_tags.append("RB")

    else:
        predicted_tags.append("NN")

print("Sentence")
print(sentence)

print("\nPredicted POS Tags\n")

for word, tag in zip(sentence, predicted_tags):
    print(word, "->", tag)
