from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
import re
import time

stemmer = PorterStemmer()

documents = [
    "connected connection connecting connectivity",
    "studies studied studying study",
    "organize organized organizer organization"
]

def normalize(text):

    words = re.findall(
        r"[a-zA-Z]+",
        text.lower()
    )

    result = []

    for word in words:
        result.append(stemmer.stem(word))

    return " ".join(result)

print("=" * 60)
print("QUESTION 5 - MORPHOLOGICAL FEATURE EXTRACTION")
print("=" * 60)

print("\nORIGINAL DOCUMENTS")

for document in documents:
    print(document)

start_before = time.time()

vectorizer_before = CountVectorizer()

X_before = vectorizer_before.fit_transform(
    documents
)

time_before = time.time() - start_before

vocabulary_before = (
    vectorizer_before.get_feature_names_out()
)

print("\nVOCABULARY BEFORE NORMALIZATION")

print(list(vocabulary_before))

print(
    "Vocabulary Size:",
    len(vocabulary_before)
)

start_after = time.time()

normalized_documents = []

for document in documents:
    normalized_documents.append(
        normalize(document)
    )

vectorizer_after = CountVectorizer()

X_after = vectorizer_after.fit_transform(
    normalized_documents
)

time_after = time.time() - start_after

vocabulary_after = (
    vectorizer_after.get_feature_names_out()
)

print("\nNORMALIZED DOCUMENTS")

for document in normalized_documents:
    print(document)

print("\nVOCABULARY AFTER NORMALIZATION")

print(list(vocabulary_after))

print(
    "Vocabulary Size:",
    len(vocabulary_after)
)

print("\nPROCESSING TIME")

print(
    "Before Normalization:",
    round(time_before, 6),
    "seconds"
)

print(
    "After Normalization:",
    round(time_after, 6),
    "seconds"
)

print("\nMORPHOLOGICAL NORMALIZATION")

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
    "organization"
]

for word in examples:
    print(
        word,
        "->",
        stemmer.stem(word)
    )

print("\nCOMPARISON")

print(
    "Vocabulary before:",
    len(vocabulary_before)
)

print(
    "Vocabulary after:",
    len(vocabulary_after)
)

reduction = (
    len(vocabulary_before)
    - len(vocabulary_after)
)

print(
    "Vocabulary reduction:",
    reduction
)

print("\nCONCLUSION")

print(
    "Morphological normalization is performed before"
)

print(
    "feature extraction."
)

print(
    "Related morphological forms can share a common stem."
)

print(
    "This reduces redundant vocabulary and can improve"
)

print(
    "machine-learning feature representation."
)

print("\n" + "=" * 60)
