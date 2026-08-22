print("=" * 60)
print("4. FEATURE STRUCTURES VS CONTEXT-FREE GRAMMAR")
print("=" * 60)

print("\nBASIC CONTEXT-FREE GRAMMAR")

print("S -> NP VP")
print("NP -> Det N")
print("VP -> V NP")

print("\nPROBLEM")
print("Basic CFG does not directly represent:")
print("Number")
print("Gender")
print("Person")
print("Tense")
print("Agreement")

print("\nFEATURE STRUCTURES")

noun_features = {
    "category": "Noun",
    "number": "singular",
    "gender": "neutral",
    "person": "third"
}

verb_features = {
    "category": "Verb",
    "tense": "present",
    "number": "singular",
    "person": "third"
}

print("\nNoun Features:")
for key, value in noun_features.items():
    print(key, "=", value)

print("\nVerb Features:")
for key, value in verb_features.items():
    print(key, "=", value)

print("\nAGREEMENT CHECK")

if (noun_features["number"] == verb_features["number"] and
        noun_features["person"] == verb_features["person"]):
    print("Agreement = Correct")
else:
    print("Agreement = Incorrect")

print("\nFEATURE STRUCTURE ADVANTAGES")
print("1. Represents grammatical information.")
print("2. Enforces subject-verb agreement.")
print("3. Handles number differences.")
print("4. Handles gender information.")
print("5. Represents person.")
print("6. Represents tense.")
print("7. Useful for multilingual grammar.")

print("\nMULTILINGUAL APPLICATION")
print("English -> Number and person")
print("Hindi -> Number, gender and person")
print("Spanish -> Number, gender and person")
print("French -> Number, gender and agreement")

print("\nCONCLUSION")
print("Feature structures extend CFG by adding grammatical features.")
print("They are useful for enforcing grammatical constraints")
print("and improving multilingual NLP systems.")

print("=" * 60)
print("ANALYSIS COMPLETED")
print("=" * 60)
