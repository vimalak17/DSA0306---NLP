import nltk
import math

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("averaged_perceptron_tagger_eng")

sentence = "Market growth drives investment."

words = nltk.word_tokenize(sentence)

initial_tags = [
    ("market", "NN"),
    ("growth", "NN"),
    ("drives", "NNS"),
    ("investment", "NN")
]

print("=" * 60)
print("FINANCIAL NEWS POS TAG CORRECTION")
print("=" * 60)

print("\nSENTENCE")
print(sentence)

print("\nTOKENS")
print(words)

print("\nINITIAL POS TAGS")

for word, tag in initial_tags:
    print(word + "/" + tag)

corrected_tags = initial_tags.copy()

for i in range(1, len(corrected_tags)):
    current_word = corrected_tags[i][0]
    current_tag = corrected_tags[i][1]
    previous_tag = corrected_tags[i - 1][1]

    if current_tag == "NNS" and previous_tag == "NN":
        corrected_tags[i] = (current_word, "VBZ")

print("\nTRANSFORMATION RULE")
print("Change NNS to VBZ if preceding word is NN.")

print("\nCORRECTED POS TAGS")

for word, tag in corrected_tags:
    print(word + "/" + tag)

frequency = {
    "market": 500,
    "growth": 350,
    "drives": 180,
    "investment": 420
}

total = sum(frequency.values())

print("\nWORD FREQUENCY")

for word, count in frequency.items():
    probability = count / total

    print(
        word,
        "Count =",
        count,
        "Probability =",
        round(probability, 4)
    )

entropy = 0

for count in frequency.values():
    probability = count / total
    entropy -= probability * math.log2(probability)

print("\nTOTAL FREQUENCY")
print(total)

print("\nENTROPY BEFORE TRANSFORMATION")
print(round(entropy, 4), "bits")

entropy_after = entropy

print("\nENTROPY AFTER TRANSFORMATION")
print(round(entropy_after, 4), "bits")

print("\nENTROPY CHANGE")
print(round(entropy_after - entropy, 4), "bits")

print("\nFINAL POS TAGGING RESULT")

for word, tag in corrected_tags:
    print(word + "/" + tag)

print("\nINTERPRETATION")
print("drives changes from NNS to VBZ.")
print("The previous word growth is tagged NN.")
print("Therefore the transformation rule is applied.")
print("Word-frequency entropy does not change because")
print("the transformation changes POS tags, not word frequencies.")

print("\n" + "=" * 60)
