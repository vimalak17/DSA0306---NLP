import nltk
import re

nltk.download("stopwords")

from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

text = """
Artificial intelligence is changing modern technology.
Machine learning is an important part of artificial intelligence.
Machine learning allows computers to learn from data.
These technologies are used in many applications.
"""

sentences = [
    sentence.strip()
    for sentence in re.split(r"[.!?]", text)
    if sentence.strip()
]

def get_keywords(sentence):
    words = re.findall(r"\b[a-zA-Z]+\b", sentence.lower())
    return {
        word for word in words
        if word not in stop_words
    }

scores = []

for i in range(len(sentences) - 1):
    words1 = get_keywords(sentences[i])
    words2 = get_keywords(sentences[i + 1])

    if words1 and words2:
        common_words = words1.intersection(words2)
        score = len(common_words) / len(words1.union(words2))
    else:
        score = 0

    scores.append(score)

if scores:
    coherence_score = sum(scores) / len(scores)
else:
    coherence_score = 0

print("Text:")
print(text)

print("Sentence-to-sentence coherence scores:")

for i, score in enumerate(scores):
    print(
        f"Sentence {i + 1} -> Sentence {i + 2}: "
        f"{score:.2f}"
    )

print(f"\nOverall Coherence Score: {coherence_score:.2f}")

if coherence_score >= 0.30:
    print("Evaluation: The text is coherent.")
elif coherence_score >= 0.15:
    print("Evaluation: The text has moderate coherence.")
else:
    print("Evaluation: The text has low coherence.")
