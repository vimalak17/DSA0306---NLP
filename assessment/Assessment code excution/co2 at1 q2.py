words = ["unhappy", "happiness", "happily"]

print("-" * 110)
print("{:<15}{:<10}{:<15}{:<15}{:<15}{:<15}".format(
    "Word", "Prefix", "Root", "Suffix", "Type", "Normalized"))
print("-" * 110)

for word in words:

    prefix = "-"
    suffix = "-"
    root = ""
    typ = "Derivational"

    if word.startswith("un"):
        prefix = "un"
        root = "happy"

    elif word.endswith("ness"):
        suffix = "ness"
        root = "happy"

    elif word.endswith("ly"):
        suffix = "ly"
        root = "happy"

    print("{:<15}{:<10}{:<15}{:<15}{:<15}{:<15}".format(
        word, prefix, root, suffix, typ, "happy"))
