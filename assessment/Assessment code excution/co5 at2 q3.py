sentences = [
    "The server crashed unexpectedly.",
    "As a result, users could not access the application.",
    "The technical team restarted the server.",
    "After that, the system became available again."
]

print("DISCOURSE UNITS")

for i, sentence in enumerate(sentences, 1):
    print("Unit", i, ":", sentence)

relations = [
    ("Unit 1", "Unit 2", "Cause-Effect"),
    ("Unit 2", "Unit 3", "Problem-Solution"),
    ("Unit 3", "Unit 4", "Sequence")
]

print("\nDISCOURSE RELATIONS")

for source, target, relation in relations:
    print(source, "->", target, ":", relation)

print("\nDISCOURSE STRUCTURE")
print("Server crashed")
print("    |")
print("    | Cause-Effect")
print("    v")
print("Users could not access application")
print("    |")
print("    | Problem-Solution")
print("    v")
print("Technical team restarted server")
print("    |")
print("    | Sequence")
print("    v")
print("System became available")
