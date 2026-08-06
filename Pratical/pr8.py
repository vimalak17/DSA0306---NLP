import random
 
pos_probabilities = {
    "I": [("PRP", 1.0)],
    "eat": [("VB", 0.8), ("NN", 0.2)],
    "rice": [("NN", 1.0)],
    "every": [("DT", 1.0)],
    "day": [("NN", 0.9), ("VB", 0.1)],
    ".": [(".", 1.0)]
}

 
sentence = "I eat rice every day ."

words = sentence.split()

print("Sentence:")
print(sentence)

print("\nStochastic POS Tags:")

for word in words:
    if word in pos_probabilities:
        tags = [tag for tag, prob in pos_probabilities[word]]
        probs = [prob for tag, prob in pos_probabilities[word]]

        # Randomly choose a tag based on probability
        selected_tag = random.choices(tags, weights=probs, k=1)[0]
    else:
        selected_tag = "NN"   # Default tag

    print(f"{word} -> {selected_tag}")
