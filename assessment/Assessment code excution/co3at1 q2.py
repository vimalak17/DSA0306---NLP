import re
from collections import Counter

corpus = """
Machine learning can solve problems.
Machine learning can predict results.
Machine learning is useful.
Machine learning is a part of artificial intelligence.
Artificial intelligence can solve problems.
Artificial intelligence can improve healthcare.
Artificial intelligence is useful.
Deep learning can solve complex problems.
Deep learning is powerful.
Natural language processing can understand language.
Natural language processing is useful.
The model can predict results.
The model learns from data.
"""

words = re.findall(r'\b[a-z]+\b', corpus.lower())

unigram = Counter(words)

bigram = Counter(
    zip(words[:-1], words[1:])
)

trigram = Counter(
    zip(words[:-2], words[1:-1], words[2:])
)

total_words = sum(unigram.values())

def p1(word):
    return unigram[word] / total_words

def p2(w1, w2):
    if unigram[w1] == 0:
        return 0
    return bigram[(w1, w2)] / unigram[w1]

def p3(w1, w2, w3):
    if bigram[(w1, w2)] == 0:
        return 0
    return trigram[(w1, w2, w3)] / bigram[(w1, w2)]

def unsmoothed(sentence):
    w = re.findall(r'\b[a-z]+\b', sentence.lower())

    result = []

    if len(w) >= 2:
        w1 = w[-2]
        w2 = w[-1]

        for triple in trigram:
            if triple[0] == w1 and triple[1] == w2:
                result.append(
                    (
                        triple[2],
                        p3(
                            triple[0],
                            triple[1],
                            triple[2]
                        )
                    )
                )

    result.sort(key=lambda x: x[1], reverse=True)

    return result[:5]

def backoff(sentence):
    w = re.findall(r'\b[a-z]+\b', sentence.lower())

    if len(w) >= 2:
        w1 = w[-2]
        w2 = w[-1]

        result = []

        for triple in trigram:
            if triple[0] == w1 and triple[1] == w2:
                result.append(
                    (
                        triple[2],
                        p3(
                            triple[0],
                            triple[1],
                            triple[2]
                        )
                    )
                )

        if result:
            result.sort(
                key=lambda x: x[1],
                reverse=True
            )
            return result[:5]

    if len(w) >= 1:
        previous = w[-1]
        result = []

        for pair in bigram:
            if pair[0] == previous:
                result.append(
                    (
                        pair[1],
                        p2(pair[0], pair[1])
                    )
                )

        if result:
            result.sort(
                key=lambda x: x[1],
                reverse=True
            )
            return result[:5]

    result = []

    for word in unigram:
        result.append(
            (word, p1(word))
        )

    result.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return result[:5]

l1 = 0.2
l2 = 0.3
l3 = 0.5

def interpolation(w1, w2, word):
    return (
        l1 * p1(word)
        + l2 * p2(w2, word)
        + l3 * p3(w1, w2, word)
    )

def interpolation_prediction(sentence):
    w = re.findall(r'\b[a-z]+\b', sentence.lower())

    if len(w) < 2:
        return []

    w1 = w[-2]
    w2 = w[-1]

    result = []

    for word in unigram:
        probability = interpolation(
            w1,
            w2,
            word
        )

        result.append(
            (word, probability)
        )

    result.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return result[:5]

sentence = input(
    "Enter incomplete sentence: "
)

print()
print("UNSMOOTHED MODEL")

result = unsmoothed(sentence)

if result:
    for word, probability in result:
        print(
            word,
            "Probability =",
            round(probability, 4)
        )
else:
    print("No prediction found")

print()
print("BACKOFF MODEL")

result = backoff(sentence)

for word, probability in result:
    print(
        word,
        "Probability =",
        round(probability, 4)
    )

print()
print("DELETED INTERPOLATION MODEL")

result = interpolation_prediction(sentence)

for word, probability in result:
    print(
        word,
        "Probability =",
        round(probability, 4)
    )

print()
print("ZERO PROBABILITY TEST")

print(
    "Trigram probability =",
    p3(
        "machine",
        "learning",
        "banana"
    )
)
