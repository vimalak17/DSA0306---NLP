import re

 
sentence = "The boys are playing happily with two dogs"

 
words = sentence.split()

print("Sentence:")
print(sentence)

print("\nRule-Based POS Tags:")

 
for word in words:

    if re.fullmatch(r"(a|an|the)", word.lower()):
        tag = "DT"          # Determiner

    elif re.fullmatch(r"(is|am|are|was|were)", word.lower()):
        tag = "VB"          # Verb

    elif re.fullmatch(r".*ing", word.lower()):
        tag = "VBG"         # Verb (Present Participle)

    elif re.fullmatch(r".*ly", word.lower()):
        tag = "RB"          # Adverb

    elif re.fullmatch(r"(one|two|three|four|five)", word.lower()):
        tag = "CD"          # Cardinal Number

    elif re.fullmatch(r".*s", word.lower()):
        tag = "NNS"         # Plural Noun

    else:
        tag = "NN"          # Default Noun

    print(word, "->", tag)
