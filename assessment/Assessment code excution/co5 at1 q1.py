entities = ["Ravi", "Arun", "book"]

references = {
    "He": ["Ravi", "Arun"],
    "it": ["book"],
    "him": ["Ravi", "Arun"],
    "they": ["Ravi", "Arun"]
}

resolved = {
    "He": "Arun",
    "it": "book",
    "him": "Ravi",
    "they": "Ravi and Arun"
}

print("REFERRING EXPRESSIONS")
print("-" * 40)

for expression, antecedents in references.items():
    print(expression, "->", antecedents)

print("\nRESOLVED REFERENCES")
print("-" * 40)

for expression, antecedent in resolved.items():
    print(expression, "->", antecedent)

print("\nCOREFERENCE CHAINS")
print("-" * 40)

print("Ravi -> him")
print("Arun -> He")
print("book -> it -> the book")
print("Ravi + Arun -> they")

print("\nRESOLVED PARAGRAPH")
print("-" * 40)

print("Ravi met Arun at the library.")
print("Arun was looking for a book on Artificial Intelligence.")
print("Arun helped Ravi find the book.")
print("Later, Ravi and Arun discussed the book before leaving.")
