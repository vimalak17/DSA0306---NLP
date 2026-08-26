import nltk
from nltk import word_tokenize, pos_tag, RegexpParser

# Download required NLTK data
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger_eng")

sentence = "The intelligent student reads a useful book in the library."

# Tokenize and POS tag
words = word_tokenize(sentence)
tagged_words = pos_tag(words)

# Grammar for noun phrases
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
"""

parser = RegexpParser(grammar)
tree = parser.parse(tagged_words)

print("Sentence:")
print(sentence)

print("\nNoun Phrases and Meanings:")

for subtree in tree.subtrees(filter=lambda t: t.label() == "NP"):
    phrase = " ".join(word for word, tag in subtree.leaves())

    # Simple semantic interpretation
    if "student" in phrase.lower():
        meaning = "A person who studies."
    elif "book" in phrase.lower():
        meaning = "A written or printed work."
    elif "library" in phrase.lower():
        meaning = "A place containing books and learning resources."
    else:
        meaning = "A noun phrase representing an entity or concept."

    print(f"Noun Phrase: {phrase}")
    print(f"Meaning: {meaning}\n")
