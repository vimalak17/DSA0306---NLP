import nltk

nltk.download("punkt")

words = [
    "treatment",
    "treatable",
    "retreatment",
    "treated",
    "untreated"
]

analyses = {
    "treatment": ["", "treat", "ment"],
    "treatable": ["", "treat", "able"],
    "retreatment": ["re", "treat", "ment"],
    "treated": ["", "treat", "ed"],
    "untreated": ["un", "treat", "ed"]
}

affix_type = {
    "re": "Derivational",
    "un": "Derivational",
    "ment": "Derivational",
    "able": "Derivational",
    "ed": "Inflectional"
}

print("=" * 70)
print("QUESTION 1 - BIOMEDICAL MORPHOLOGICAL ANALYSIS")
print("=" * 70)

for word in words:

    prefix = analyses[word][0]
    root = analyses[word][1]
    suffix = analyses[word][2]

    print("\nWord:", word)

    if prefix:
        print("Prefix:", prefix)
        print("Prefix Type:", affix_type[prefix])
    else:
        print("Prefix: None")

    print("Root:", root)

    if suffix:
        print("Suffix:", suffix)
        print("Suffix Type:", affix_type[suffix])
    else:
        print("Suffix: None")

    parts = []

    if prefix:
        parts.append(prefix)

    parts.append(root)

    if suffix:
        parts.append(suffix)

    print("Decomposition:", " + ".join(parts))

print("\nSUMMARY")

print("treatment = treat + ment")
print("treatable = treat + able")
print("retreatment = re + treat + ment")
print("treated = treat + ed")
print("untreated = un + treat + ed")

print("\nInterpretation")
print("Derivational affixes change meaning or word class.")
print("Inflectional affixes express grammatical information.")
print("Correct morphological analysis improves biomedical search.")
