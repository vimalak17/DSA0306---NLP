words = ["played", "player", "playing"]

print("-" * 110)
print("{:<15}{:<15}{:<15}{:<18}{:<15}".format(
    "Word", "Stem", "Removed", "Transformation", "Normalized"))
print("-" * 110)

for word in words:

    if word.endswith("ed"):
        stem = word[:-2]
        affix = "ed"
        typ = "Inflectional"

    elif word.endswith("ing"):
        stem = word[:-3]
        affix = "ing"
        typ = "Inflectional"

    elif word.endswith("er"):
        stem = word[:-2]
        affix = "er"
        typ = "Derivational"

    else:
        stem = word
        affix = "-"
        typ = "-"

    print("{:<15}{:<15}{:<15}{:<18}{:<15}".format(
        word, stem, affix, typ, stem))
