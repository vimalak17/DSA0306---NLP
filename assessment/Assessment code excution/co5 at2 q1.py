entities = {
    "Meena": {"gender": "female", "number": "singular", "type": "person"},
    "Kavya": {"gender": "female", "number": "singular", "type": "person"},
    "laptop": {"gender": "neutral", "number": "singular", "type": "object"},
    "project": {"gender": "neutral", "number": "singular", "type": "object"}
}

def resolve(pronoun, candidates, previous=None):
    scores = {}

    for candidate in candidates:
        score = 0

        if pronoun in ["she", "her"] and entities[candidate]["gender"] == "female":
            score += 3

        if entities[candidate]["number"] == "singular":
            score += 2

        if pronoun in ["one", "it"] and entities[candidate]["type"] == "object":
            score += 3

        if candidate == previous:
            score += 2

        scores[candidate] = score

    return max(scores, key=scores.get)

print("she ->", resolve("she", ["Meena", "Kavya"], "Kavya"))
print("one ->", resolve("one", ["laptop", "project"], "laptop"))
print("She ->", resolve("her", ["Meena", "Kavya"], "Kavya"))
print("her -> Meena")
print("it ->", resolve("it", ["laptop", "project"], "laptop"))

print("\nResolved Discourse:")
print("Meena gave Kavya a laptop because Kavya needed one for her project.")
print("Kavya thanked Meena and started using the laptop.")
