import nltk

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("averaged_perceptron_tagger_eng")

from nltk.tokenize import word_tokenize
from nltk import pos_tag

sentence1 = "Book an appointment with the doctor."
sentence2 = "The book contains medical information."

print("=" * 60)
print("AI-POWERED HOSPITAL APPOINTMENT CHATBOT")
print("=" * 60)

tokens1 = word_tokenize(sentence1)
tokens2 = word_tokenize(sentence2)

print("\nSENTENCE 1")
print(sentence1)

print("\nTOKENS")
print(tokens1)

print("\nPOS TAGS")
print(pos_tag(tokens1))

print("\nSENTENCE 2")
print(sentence2)

print("\nTOKENS")
print(tokens2)

print("\nPOS TAGS")
print(pos_tag(tokens2))

p_book_vb = 0.7
p_book_nn = 0.3

p_start_vb = 0.6
p_start_nn = 0.4

prob_vb = p_start_vb * p_book_vb
prob_nn = p_start_nn * p_book_nn

print("\nHMM CALCULATION")

print(
    "P(book | VB) =",
    p_book_vb
)

print(
    "P(book | NN) =",
    p_book_nn
)

print(
    "P(Start -> VB) =",
    p_start_vb
)

print(
    "P(Start -> NN) =",
    p_start_nn
)

print(
    "P(VB, book) =",
    p_start_vb,
    "*",
    p_book_vb,
    "=",
    prob_vb
)

print(
    "P(NN, book) =",
    p_start_nn,
    "*",
    p_book_nn,
    "=",
    prob_nn
)

if prob_vb > prob_nn:
    best_tag = "VB"
else:
    best_tag = "NN"

print("\nMOST PROBABLE TAG FOR 'BOOK'")
print(best_tag)

print("\nFINAL CONTEXT-BASED INTERPRETATION")

print(
    "Sentence 1: Book = VB because it is an action."
)

print(
    "Sentence 2: book = NN because it is a noun."
)

print("\n" + "=" * 60)
