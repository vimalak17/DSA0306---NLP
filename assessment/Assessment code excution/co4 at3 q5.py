print("=" * 60)
print("5. SUBCATEGORIZATION FRAMES")
print("=" * 60)

verbs = {
    "give": {
        "frame": "Verb + Object + Recipient",
        "example": "Give the book to John",
        "arguments": ["book", "John"]
    },
    "sleep": {
        "frame": "Verb only",
        "example": "Sleep",
        "arguments": []
    },
    "put": {
        "frame": "Verb + Object + Location",
        "example": "Put the file on the desk",
        "arguments": ["file", "desk"]
    }
}

print("\nVERB: GIVE")
print("Example:", verbs["give"]["example"])
print("Frame:", verbs["give"]["frame"])
print("Object:", verbs["give"]["arguments"][0])
print("Recipient:", verbs["give"]["arguments"][1])

print("\nVERB: SLEEP")
print("Example:", verbs["sleep"]["example"])
print("Frame:", verbs["sleep"]["frame"])
print("Arguments: None")

print("\nVERB: PUT")
print("Example:", verbs["put"]["example"])
print("Frame:", verbs["put"]["frame"])
print("Object:", verbs["put"]["arguments"][0])
print("Location:", verbs["put"]["arguments"][1])

print("\nIMPORTANCE OF SUBCATEGORIZATION")
print("1. Identifies required verb arguments.")
print("2. Determines valid sentence structures.")
print("3. Helps detect missing arguments.")
print("4. Helps identify incorrect arguments.")
print("5. Supports semantic role labeling.")
print("6. Improves syntactic parsing.")
print("7. Helps conversational AI understand commands.")

print("\nEXAMPLE VALIDATION")

sentence1 = ["give", "book", "John"]
sentence2 = ["sleep"]
sentence3 = ["put", "file", "desk"]

if len(sentence1) == 3:
    print("Give -> Valid argument structure")

if len(sentence2) == 1:
    print("Sleep -> Valid argument structure")

if len(sentence3) == 3:
    print("Put -> Valid argument structure")

print("\nCONCLUSION")
print("Subcategorization frames specify the arguments required by verbs.")
print("They are important for both syntactic and semantic analysis.")
print("They help voice assistants correctly understand user commands.")

print("=" * 60)
print("ANALYSIS COMPLETED")
print("=" * 60)
