import nltk

nltk.download("wordnet")
nltk.download("omw-1.4")

from nltk.wsd import lesk

sentence = input("Enter sentence: ")
word = input("Enter ambiguous word: ")

tokens = nltk.word_tokenize(sentence)

sense = lesk(tokens, word)

if sense:
    print("Selected Sense:", sense.name())
    print("Definition:", sense.definition())
    print("Examples:", sense.examples())
else:
    print("No sense found")
