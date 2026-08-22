prefixes = [
    "un",
    "re",
    "dis"
]

suffixes = [
    "able",
    "ing",
    "ed",
    "er",
    "s"
]

words = [
    "replayed",
    "unhappier",
    "disconnected",
    "players",
    "restarting",
    "unreadable"
]

roots = {
    "replayed": "play",
    "unhappier": "happy",
    "disconnected": "connect",
    "players": "play",
    "restarting": "start",
    "unreadable": "read"
}

def parser(word):

    original = word
    found_prefixes = []
    found_suffixes = []

    changed = True

    while changed:

        changed = False

        for prefix in prefixes:

            if word.startswith(prefix):

                if len(word) > len(prefix) + 2:

                    found_prefixes.append(prefix)

                    word = word[len(prefix):]

                    changed = True

                    break

    changed = True

    while changed:

        changed = False

        for suffix in sorted(
            suffixes,
            key=len,
            reverse=True
        ):

            if word.endswith(suffix):

                if len(word) > len(suffix) + 2:

                    found_suffixes.insert(
                        0,
                        suffix
                    )

                    word = word[:-len(suffix)]

                    changed = True

                    break

    return (
        original,
        found_prefixes,
        roots.get(original, word),
        found_suffixes
    )


print("=" * 70)
print("QUESTION 2 - FINITE-STATE MORPHOLOGICAL PARSER")
print("=" * 70)

for word in words:

    original, prefixes_found, root, suffixes_found = parser(word)

    parts = []

    for item in prefixes_found:
        parts.append(item)

    parts.append(root)

    for item in suffixes_found:
        parts.append(item)

    print("\nWord:", original)
    print("Prefixes:", prefixes_found)
    print("Root:", root)
    print("Suffixes:", suffixes_found)
    print("Analysis:", " + ".join(parts))

print("\nPARSER STRUCTURE")
print("START -> PREFIX* -> ROOT -> SUFFIX* -> END")

print("\nAccuracy Test")

correct = 0

expected = {
    "replayed": ["re", "play", "ed"],
    "unhappier": ["un", "happy", "er"],
    "disconnected": ["dis", "connect", "ed"],
    "players": ["play", "er", "s"],
    "restarting": ["re", "start", "ing"],
    "unreadable": ["un", "read", "able"]
}

for word in words:

    original, p, root, s = parser(word)

    result = p + [root] + s

    if result == expected[word]:
        correct += 1

accuracy = correct / len(words) * 100

print("Correct Analyses:", correct)
print("Total Words:", len(words))
print("Accuracy:", round(accuracy, 2), "%")
