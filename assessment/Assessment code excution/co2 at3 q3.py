import re
from nltk.stem import PorterStemmer

ps = PorterStemmer()

documents = [
    "The market is growing rapidly.",
    "The company announced a new product.",
    "Technology companies are expanding.",
    "The investors are studying the financial report.",
    "The organization organized a new meeting."
]

def process_text(text):
    tokens = re.findall(r"[a-zA-Z]+", text.lower())

    stemmed = []

    for token in tokens:
        stemmed.append(ps.stem(token))

    return tokens, stemmed

print("=" * 60)
print("QUESTION 3 - STEMMING ERROR ANALYSIS")
print("=" * 60)

for i, text in enumerate(documents):

    tokens, stemmed = process_text(text)

    print("\nDOCUMENT", i + 1)

    print("Original Text:")
    print(text)

    print("\nTokens:")
    print(tokens)

    print("\nStemmed Tokens:")
    print(stemmed)

print("\nPROBLEMATIC STEMMING CASES")

examples = [
    "connected",
    "connection",
    "connecting",
    "connectivity",
    "studies",
    "studied",
    "studying",
    "study",
    "organize",
    "organized",
    "organizer",
    "organization",
    "treatment",
    "treated",
    "readable",
    "happiness",
    "relational",
    "usefulness",
    "agreement",
    "running"
]

for word in examples:
    print(word, "->", ps.stem(word))

print("\n" + "=" * 60)
print("PROCESSING COMPLETED")
print("=" * 60)
