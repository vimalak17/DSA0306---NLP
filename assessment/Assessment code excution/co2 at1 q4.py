words = ["writes", "writing", "written"]

print("-" * 130)
print("{:<12}{:<35}{:<20}{:<15}{:<15}".format(
    "Word", "State Transition", "Pattern", "Root", "Normalized"))
print("-" * 130)

for word in words:

    if word == "writes":
        transition = "Start -> Verb -> s -> End"
        pattern = "Regular"
        root = "write"

    elif word == "writing":
        transition = "Start -> Verb -> ing -> End"
        pattern = "Regular"
        root = "write"

    elif word == "written":
        transition = "Start -> Verb -> irregular -> End"
        pattern = "Irregular"
        root = "write"

    print("{:<12}{:<35}{:<20}{:<15}{:<15}".format(
        word, transition, pattern, root, root))
