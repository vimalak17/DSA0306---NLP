import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [0.6]
NP -> N [0.4]
VP -> V NP [0.7]
VP -> V [0.3]
Det -> 'the' [0.5]
Det -> 'a' [0.5]
N -> 'cat' [0.4]
N -> 'dog' [0.3]
N -> 'milk' [0.3]
V -> 'drinks' [0.5]
V -> 'eats' [0.5]
""")

sentence = input("Enter sentence: ").lower().split()

parser = ViterbiParser(grammar)
trees = list(parser.parse(sentence))

if trees:
    print("Most probable parse:")
    print(trees[0])
    print("Probability:", trees[0].prob())
else:
    print("No valid parse found")
