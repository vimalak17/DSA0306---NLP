import nltk
from nltk.corpus import wordnet
nltk.download('Wordnet')
nltk.download('omw-1.4')
word="car"
synsets=wordnet.synsets(word)
print("Word:",word)
print("Number of synsets:", len(synsets))
for synset in synsets:
    print("\nsynset:",synset.name())
    print("Definition:",synset.definition())
    print("Examples:",synset.examples())
    synonyms=synset.lemmas()
    print("synonyms:",[lemma.name() for lemma in synonyms])
