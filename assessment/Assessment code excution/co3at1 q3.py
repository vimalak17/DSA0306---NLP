import re
import math
from collections import Counter

training_text = """
The cat sits on the mat.
The cat eats fish.
The dog sits on the mat.
The dog eats food.
The boy reads a book.
The girl reads a book.
The student studies machine learning.
Machine learning is useful.
Artificial intelligence is useful.
The model learns from data.
The model predicts results.
Natural language processing is useful.
"""

testing_text = [
    "The cat sits on the mat.",
    "The dog eats food.",
    "The student studies machine learning.",
    "The quantum processor redesigned the system."
]

train_words = re.findall(r'\b[a-z]+\b', training_text.lower())

unigram = Counter(train_words)

bigram = Counter(
    zip(train_words[:-1], train_words[1:])
)

trigram = Counter(
    zip(train_words[:-2], train_words[1:-1], train_words[2:])
)

total_words = len(train_words)
vocabulary_size = len(unigram)

def unigram_probability(word):
    return unigram[word] / total_words

def bigram_probability(w1, w2):
    if unigram[w1] == 0:
        return 0
    return bigram[(w1, w2)] / unigram[w1]

def trigram_probability(w1, w2, w3):
    if bigram[(w1, w2)] == 0:
        return 0
    return trigram[(w1, w2, w3)] / bigram[(w1, w2)]

def smoothed_trigram_probability(w1, w2, w3):
    return (
        trigram[(w1, w2, w3)] + 1
    ) / (
        bigram[(w1, w2)] + vocabulary_size
    )

def calculate_entropy(sentence, model):
    words = re.findall(
        r'\b[a-z]+\b',
        sentence.lower()
    )

    total_entropy = 0
    word_count = 0

    for i in range(len(words)):

        if model == "unigram":
            probability = unigram_probability(words[i])

        elif model == "bigram":
            if i == 0:
                probability = unigram_probability(words[i])
            else:
                probability = bigram_probability(
                    words[i - 1],
                    words[i]
                )

        elif model == "trigram":
            if i < 2:
                probability = unigram_probability(words[i])
            else:
                probability = trigram_probability(
                    words[i - 2],
                    words[i - 1],
                    words[i]
                )

        elif model == "smoothed":
            if i < 2:
                probability = unigram_probability(words[i])
            else:
                probability = smoothed_trigram_probability(
                    words[i - 2],
                    words[i - 1],
                    words[i]
                )

        if probability == 0:
            return float("inf")

        total_entropy += -math.log2(probability)
        word_count += 1

    return total_entropy / word_count


for sentence in testing_text:

    print()
    print("Sentence:")
    print(sentence)

    print()
    print("Unigram Entropy:")

    value = calculate_entropy(
        sentence,
        "unigram"
    )

    if math.isinf(value):
        print("Infinity")
    else:
        print(round(value, 4))

    print()
    print("Bigram Entropy:")

    value = calculate_entropy(
        sentence,
        "bigram"
    )

    if math.isinf(value):
        print("Infinity")
    else:
        print(round(value, 4))

    print()
    print("Trigram Entropy:")

    value = calculate_entropy(
        sentence,
        "trigram"
    )

    if math.isinf(value):
        print("Infinity")
    else:
        print(round(value, 4))

    print()
    print("Smoothed Trigram Entropy:")

    value = calculate_entropy(
        sentence,
        "smoothed"
    )

    if math.isinf(value):
        print("Infinity")
    else:
        print(round(value, 4))

    print()
    print("--------------------------------")

print()
print("INTERPRETATION")
print("Low entropy means the sentence is predictable.")
print("High entropy means the sentence is unpredictable.")
print("Infinity means an unseen word sequence has probability zero.")
print("Smoothing reduces the zero-probability problem.")
