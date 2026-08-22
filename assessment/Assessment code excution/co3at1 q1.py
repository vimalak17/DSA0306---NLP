import re
from collections import Counter

corpus = """
Artificial intelligence is changing the world.
Artificial intelligence is useful in many applications.
Artificial intelligence is used in healthcare.
Artificial intelligence is used in education.
Machine learning is a part of artificial intelligence.
Machine learning can solve many problems.
Machine learning can predict future results.
Deep learning is a powerful machine learning method.
Natural language processing is a branch of artificial intelligence.
Natural language processing can understand human language.
The computer learns from data.
The model predicts the next word.
The model learns from training data.
Data science is useful for business.
Data science uses machine learning methods.
The student learns artificial intelligence.
The student studies machine learning.
"""

def preprocess(text):
    text = text.lower()
    sentences = re.split(r'[.!?]+', text)
    result = []

    for sentence in sentences:
        words = re.findall(r'\b[a-z]+\b', sentence)
        if words:
            result.append(words)

    return result

sentences = preprocess(corpus)

unigram = Counter()
bigram = Counter()
trigram = Counter()

for sentence in sentences:
    for word in sentence:
        unigram[word] += 1

    for i in range(len(sentence) - 1):
        bigram[(sentence[i], sentence[i + 1])] += 1

    for i in range(len(sentence) - 2):
        trigram[(sentence[i], sentence[i + 1], sentence[i + 2])] += 1

total_words = sum(unigram.values())

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

def predict_unigram():
    result = []

    for word in unigram:
        result.append((word, unigram_probability(word)))

    result.sort(key=lambda x: x[1], reverse=True)

    return result[:5]

def predict_bigram(word):
    result = []

    for pair in bigram:
        if pair[0] == word:
            probability = bigram_probability(pair[0], pair[1])
            result.append((pair[1], probability))

    result.sort(key=lambda x: x[1], reverse=True)

    return result[:5]

def predict_trigram(w1, w2):
    result = []

    for triple in trigram:
        if triple[0] == w1 and triple[1] == w2:
            probability = trigram_probability(
                triple[0], triple[1], triple[2]
            )
            result.append((triple[2], probability))

    result.sort(key=lambda x: x[1], reverse=True)

    return result[:5]

print("N-GRAM LANGUAGE MODEL")
print()
print("1. Unigram")
print("2. Bigram")
print("3. Trigram")

n = int(input("Enter N (1, 2 or 3): "))

sentence = input("Enter incomplete sentence: ").lower()
words = re.findall(r'\b[a-z]+\b', sentence)

if n == 1:
    predictions = predict_unigram()

elif n == 2:
    if len(words) >= 1:
        predictions = predict_bigram(words[-1])
    else:
        predictions = []

elif n == 3:
    if len(words) >= 2:
        predictions = predict_trigram(words[-2], words[-1])
    else:
        predictions = []

else:
    print("Invalid N")
    predictions = []

print()
print("Top 5 Predictions")

if len(predictions) == 0:
    print("No prediction found")
else:
    for word, probability in predictions:
        print(word, "Probability =", round(probability, 4))

print()
print("N-GRAM FREQUENCY COUNTS")

print()
print("Unigrams:")
for word, count in unigram.most_common(10):
    print(word, "=", count)

print()
print("Bigrams:")
for pair, count in bigram.most_common(10):
    print(pair, "=", count)

print()
print("Trigrams:")
for triple, count in trigram.most_common(10):
    print(triple, "=", count)

print()
print("UNSEEN N-GRAM TEST")

print(
    "Bigram probability:",
    bigram_probability("quantum", "processor")
)

print(
    "Trigram probability:",
    trigram_probability(
        "quantum",
        "processor",
        "redesigned"
    )
)

print()
print("Accuracy Test")

test_data = [
    ("artificial intelligence", "is"),
    ("machine learning", "is"),
    ("natural language", "processing"),
    ("data science", "is")
]

correct = 0
total = 0

for first, second in test_data:
    prediction = predict_trigram(first, second)

    if len(prediction) > 0:
        predicted_words = [x[0] for x in prediction]

        if second in predicted_words:
            correct += 1

        total += 1

if total > 0:
    accuracy = correct / total * 100
    print("Accuracy =", round(accuracy, 2), "%")
else:
    print("Accuracy cannot be calculated")
