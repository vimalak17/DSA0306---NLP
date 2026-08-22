import nltk
import numpy as np
import math
from collections import Counter
from nltk.util import ngrams
nltk.download("punkt")
corpus = "machine learning improves business, machine learning enables automation, machine learning drives innovation."

words = nltk.word_tokenize(corpus.lower())

unigram = Counter(words)
bigram = Counter(ngrams(words, 2))
trigram = Counter(ngrams(words, 3))

total_words = len(words)

print("=" * 60)
print("E-COMMERCE SMART SEARCH AND PRODUCT PREDICTION")
print("=" * 60)

print("\nCORPUS")
print(corpus)

print("\nUNIGRAM COUNTS")
for word, count in unigram.items():
    print(word, "=", count)

print("\nBIGRAM COUNTS")
for pair, count in bigram.items():
    print(pair, "=", count)

print("\nTRIGRAM COUNTS")
for triple, count in trigram.items():
    print(triple, "=", count)

p_learning_machine = (
    bigram[("machine", "learning")]
    / unigram["machine"]
)

print("\n1. MLE BIGRAM PROBABILITY")
print("C(machine) =", unigram["machine"])
print(
    "C(machine, learning) =",
    bigram[("machine", "learning")]
)
print(
    "P(learning | machine) =",
    p_learning_machine
)

print("\n2. BACKOFF MODEL")

trigram_probability = 0

if ("machine", "learning", "transforms") in trigram:
    trigram_probability = (
        trigram[("machine", "learning", "transforms")]
        / bigram[("machine", "learning")]
    )

print(
    "P(transforms | machine, learning) =",
    trigram_probability
)

if unigram["learning"] > 0:
    bigram_probability = (
        bigram[("learning", "transforms")]
        / unigram["learning"]
    )
else:
    bigram_probability = 0

print(
    "P(transforms | learning) =",
    bigram_probability
)

unigram_probability = (
    unigram["transforms"] / total_words
)

print(
    "P(transforms) =",
    unigram_probability
)

backoff_probability = max(
    trigram_probability,
    bigram_probability,
    unigram_probability
)

print(
    "Final Backoff Probability =",
    backoff_probability
)

print("\n3. DELETED INTERPOLATION")

lambda1 = 0.5
lambda2 = 0.3
lambda3 = 0.2

p_tri = 1 / 3
p_bi = 1 / 3
p_uni = 1 / total_words

print("Lambda 1 =", lambda1)
print("Lambda 2 =", lambda2)
print("Lambda 3 =", lambda3)

print("Trigram probability =", p_tri)
print("Bigram probability =", p_bi)
print("Unigram probability =", p_uni)

interpolation_probability = (
    lambda1 * p_tri
    + lambda2 * p_bi
    + lambda3 * p_uni
)

print(
    "Interpolated Probability =",
    interpolation_probability
)

print("\n4. ENTROPY")

prediction_probabilities = np.array(
    [0.33, 0.33, 0.33]
)

entropy = 0

for probability in prediction_probabilities:
    entropy -= probability * math.log2(probability)

print(
    "Prediction probabilities:",
    prediction_probabilities
)

print(
    "Entropy =",
    round(entropy, 4)
)

print("\n5. FINAL NEXT-WORD PREDICTION")

predictions = {
    "improves": 0.33,
    "enables": 0.33,
    "drives": 0.33
}

sorted_predictions = sorted(
    predictions.items(),
    key=lambda x: x[1],
    reverse=True
)

for word, probability in sorted_predictions:
    print(
        word,
        "->",
        probability
    )

print("\nMost probable next words:")
print("improves, enables, drives")

print("\n" + "=" * 60)
