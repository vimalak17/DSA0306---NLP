text = [
    "Anjali bought a new laptop.",
    "The laptop had a powerful processor.",
    "She installed Python on it.",
    "Later, Anjali used the computer to develop a machine learning application."
]

chains = {
    "Anjali": [(1, "Anjali"), (3, "She"), (4, "Anjali")],
    "Laptop": [(1, "laptop"), (2, "The laptop"), (3, "it"), (4, "the computer")],
    "Processor": [(2, "processor")],
    "Python": [(3, "Python")],
    "Application": [(4, "machine learning application")]
}

print("ENTITY CHAINS")

for entity, references in chains.items():
    print(entity, "->", [ref for _, ref in references])

repeated_entities = sum(
    1 for references in chains.values() if len(references) > 1
)

total_entities = len(chains)

coherence = (repeated_entities / total_entities) * 100

print("\nCoherence Score:", round(coherence, 2), "%")

if coherence >= 40:
    print("Discourse is COHERENT")
else:
    print("Discourse has LOW COHERENCE")
