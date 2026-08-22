print("=" * 60)
print("WORD SENSE DISAMBIGUATION")
print("TRAVEL RECOMMENDATION SYSTEM")
print("=" * 60)

queries = [
    ("Amazon tour",
     "Amazon rainforest",
     "Viewed rainforest trekking packages"),

    ("Safari booking",
     "Wildlife tour",
     "Selected wildlife resort packages"),

    ("Java vacation",
     "Java island",
     "Viewed hotels in Bali and Java"),

    ("Cruise package",
     "Ship journey",
     "Viewed Mediterranean ship packages"),

    ("Safari download for Windows",
     "Web browser",
     "Clicked a browser download page")
]

print("\nTASK 1")

for query, sense, evidence in queries:
    print("\nQuery:", query)
    print("Intended Sense:", sense)
    print("User Interaction:", evidence)

print("\nTASK 2")
print("""
Amazon + tour + rainforest -> Amazon rainforest

Safari + booking + wildlife resort -> Wildlife tour

Java + vacation + hotels -> Java island

Cruise + Mediterranean + ship -> Ship journey

Safari + download + Windows -> Web browser
""")

print("TASK 3")
print("""
The same word can have different meanings.

Safari can mean:
1. Wildlife safari
2. Safari web browser

For example:

Safari booking -> Wildlife tour

Safari download for Windows -> Web browser

Therefore, the intended meaning depends on the query,
context and user behaviour.
""")

print("TASK 4")
print("""
An industrial WSD system can use:

1. Query Context
2. User Search History
3. User Browsing History
4. Click Behaviour
5. Word Embeddings
6. Transformer Models such as BERT
7. Semantic Similarity
8. Recommendation Feedback

Process:

User Query
    |
    v
Identify Ambiguous Word
    |
    v
Analyze Context
    |
    v
Use Embeddings
    |
    v
Check User History
    |
    v
Analyze Click Behaviour
    |
    v
Select Most Probable Sense
    |
    v
Generate Recommendation
""")

print("=" * 60)
print("WSD ANALYSIS COMPLETED")
print("=" * 60)
