import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

import nltk
from nltk.tokenize import word_tokenize

text = "The cat is sitting on the mat."

words = word_tokenize(text)

tagged = nltk.pos_tag(words)

print("Sentence:")
print(text)

print("\nPOS Tags:")
for word, tag in tagged:
    print(word, "->", tag)
