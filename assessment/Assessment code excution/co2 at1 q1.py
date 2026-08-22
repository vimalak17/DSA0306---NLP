words = ["connected", "connecting", "connection"]

print("-" * 90)
print("{:<15}{:<15}{:<15}{:<15}{:<15}".format(
    "Word", "Root", "Suffix", "Type", "Normalized"))
print("-" * 90)

for word in words:

    if word.endswith("ed"):
        root = word[:-2]
        suffix = "ed"
        typ = "Inflectional"
        normalized = "connect"

    elif word.endswith("ing"):
        root = word[:-3]
        suffix = "ing"
        typ = "Inflectional"
        normalized = "connect"

    elif word.endswith("ion"):
        root = word[:-3]
        suffix = "ion"
        typ = "Derivational"
        normalized = "connect"

    else:
        root = word
        suffix = "-"
        typ = "-"
        normalized = word

    print("{:<15}{:<15}{:<15}{:<15}{:<15}".format(
        word, root, suffix, typ, normalized))
