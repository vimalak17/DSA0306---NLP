import nltk

nltk.download("wordnet")
nltk.download("omw-1.4")

from nltk.corpus import wordnet

irregular = {
    "children": "child",
    "men": "man",
    "women": "woman",
    "mice": "mouse",
    "geese": "goose",
    "feet": "foot",
    "teeth": "tooth",
    "people": "person"
}

def old_parser(word):
    if word.endswith("s"):
        return word[:-2], "Plural Noun"
    else:
        return word, "Singular"


def parser(word):

    if word in irregular:
        return irregular[word], "Plural Noun"

    if word.endswith("ies"):
        return word[:-3] + "y", "Plural Noun"

    if word.endswith("es"):
        return word[:-2], "Plural Noun"

    if word.endswith("s"):
        return word[:-1], "Plural Noun"

    return word, "Singular"


words = [
    "cars",
    "boxes",
    "cities",
    "children",
    "books",
    "men",
    "women",
    "mice",
    "dogs",
    "classes"
]

print("=" * 60)
print("QUESTION 4 - PLURAL NOUN PARSER")
print("=" * 60)

print("\nORIGINAL PARSER OUTPUT")

for word in words:
    root, tag = old_parser(word)
    print(word, "->", root, ",", tag)

print("\nCORRECTED PARSER OUTPUT")

for word in words:
    root, tag = parser(word)
    print(word, "->", root, ",", tag)

print("\nWORDNET CHECK")

for word in words:

    synsets = wordnet.synsets(
        word,
        pos=wordnet.NOUN
    )

    if len(synsets) > 0:
        print(word, "-> WordNet entry found")
    else:
        print(word, "-> WordNet entry not found")

print("\nRULES")

print("Regular plural: books -> book")
print("ES plural: boxes -> box")
print("IES plural: cities -> city")
print("Irregular plural: children -> child")

print("\n" + "=" * 60)
