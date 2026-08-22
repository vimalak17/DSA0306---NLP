import nltk
from nltk.corpus import brown
from nltk.tag import UnigramTagger
from nltk.tag import BigramTagger

nltk.download("brown")
nltk.download("universal_tagset")

data = brown.tagged_sents(tagset="universal")

split = int(len(data) * 0.8)

train = data[:split]
test = data[split:]

def rule_tag(word):
    word = word.lower()

    dictionary = {
        "i": "PRON",
        "you": "PRON",
        "he": "PRON",
        "she": "PRON",
        "we": "PRON",
        "they": "PRON",
        "a": "DET",
        "an": "DET",
        "the": "DET",
        "is": "VERB",
        "am": "VERB",
        "are": "VERB",
        "was": "VERB",
        "were": "VERB",
        "and": "CONJ",
        "or": "CONJ",
        "in": "ADP",
        "on": "ADP",
        "at": "ADP",
        "book": "NOUN",
        "ticket": "NOUN",
        "read": "VERB"
    }

    if word in dictionary:
        return dictionary[word]

    if word.endswith("ing"):
        return "VERB"

    if word.endswith("ed"):
        return "VERB"

    if word.endswith("ly"):
        return "ADV"

    if word.endswith("ous"):
        return "ADJ"

    if word.endswith("ful"):
        return "ADJ"

    if word.endswith("ness"):
        return "NOUN"

    if word.isdigit():
        return "NUM"

    return "NOUN"

def rule_based(sentence):
    words = sentence.split()
    result = []

    for word in words:
        result.append((word, rule_tag(word)))

    return result

unigram_tagger = UnigramTagger(train)

bigram_tagger = BigramTagger(
    train,
    backoff=unigram_tagger
)

def initial_tag(word):
    word = word.lower()

    if word in ["a", "an", "the"]:
        return "DET"

    if word in ["i", "you", "he", "she", "we", "they"]:
        return "PRON"

    if word.endswith("ing"):
        return "VERB"

    if word.endswith("ed"):
        return "VERB"

    if word.endswith("ly"):
        return "ADV"

    return "NOUN"

def transformation(sentence):
    words = sentence.split()

    tags = []

    for word in words:
        tags.append(initial_tag(word))

    for i in range(len(words)):
        word = words[i].lower()

        if word == "book":
            if i > 0:
                previous = words[i - 1].lower()

                if previous in ["a", "an", "the"]:
                    tags[i] = "NOUN"
                else:
                    tags[i] = "VERB"

        if word == "read":
            if i > 0:
                previous = words[i - 1].lower()

                if previous in [
                    "i",
                    "you",
                    "he",
                    "she",
                    "we",
                    "they"
                ]:
                    tags[i] = "VERB"

    return list(zip(words, tags))

sentence = input("Enter an English sentence: ")

print()
print("RULE-BASED POS TAGGING")
print(rule_based(sentence))

print()
print("STOCHASTIC POS TAGGING")
print(bigram_tagger.tag(sentence.split()))

print()
print("TRANSFORMATION-BASED POS TAGGING")
print(transformation(sentence))

print()
print("CONTEXT EXAMPLE")

sentence1 = "I book a ticket."
sentence2 = "I read a book."

print()
print(sentence1)
print("Rule-Based:", rule_based(sentence1))
print("Stochastic:", bigram_tagger.tag(sentence1.split()))
print("Transformation:", transformation(sentence1))

print()
print(sentence2)
print("Rule-Based:", rule_based(sentence2))
print("Stochastic:", bigram_tagger.tag(sentence2.split()))
print("Transformation:", transformation(sentence2))

correct = 0
total = 0

for sentence_data in test:

    words = []

    actual = []

    for word, tag in sentence_data:
        words.append(word)
        actual.append(tag)

    predicted = bigram_tagger.tag(words)

    for i in range(len(actual)):
        if predicted[i][1] == actual[i]:
            correct += 1

        total += 1

accuracy = (correct / total) * 100

print()
print("STOCHASTIC TAGGER ACCURACY")
print(round(accuracy, 2), "%")
