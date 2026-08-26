sentence = "Priya sat on the bank and watched the boats moving across the water."

possible_senses = [
    "Financial institution",
    "Side of a river"
]

context_words = [
    "sat",
    "boats",
    "water",
    "moving"
]

river_words = ["boats", "water", "river", "shore"]

financial_words = ["money", "account", "cash", "loan"]

river_score = 0
financial_score = 0

for word in context_words:
    if word in river_words:
        river_score += 1

    if word in financial_words:
        financial_score += 1

if river_score > financial_score:
    selected_sense = "Side of a river"
else:
    selected_sense = "Financial institution"

print("WORD SENSE DISAMBIGUATION")
print("-" * 40)

print("Sentence:", sentence)

print("\nPossible meanings:")
for sense in possible_senses:
    print("-", sense)

print("\nSelected meaning:")
print(selected_sense)

print("\nPredicate Logic")
print("-" * 40)

print("sit(Priya, Bank)")
print("bank(Bank)")
print("beside(Priya, Bank)")
print("watch(Priya, Boat)")
print("boat(Boat)")
print("move(Boat)")
print("water(Water)")
print("across(Boat, Water)")

print("\nUnambiguous Paraphrase")
print("-" * 40)

print("Priya sat beside the river and watched boats moving across the water.")

print("\nReason")
print("-" * 40)

print("The words boats and water indicate that bank means the side of a river.")
print("WSD helps machine translation choose the correct meaning of ambiguous words.")
