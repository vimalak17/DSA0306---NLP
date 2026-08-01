import nltk
from nltk.stem import PorterStemmer
nltk.download('punkt') 
stemmer = PorterStemmer()
words = [
    "running",
    "playing",
    "studies",
    "connected",
    "happiness",
    "cars"
]

print("Original Word\tStemmed Word") 
for word in words:
    stem = stemmer.stem(word)
    print(f"{word:15}{stem}")
