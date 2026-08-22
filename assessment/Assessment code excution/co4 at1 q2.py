print("=" * 60)
print("FIRST-ORDER PREDICATE CALCULUS")
print("SMART AGRICULTURE")
print("=" * 60)

fields = {
    "F1": {"soil": "Dry", "irrigation": "Available", "crop": "Rice"},
    "F2": {"soil": "Wet", "irrigation": "Available", "crop": "Wheat"},
    "F3": {"soil": "Dry", "irrigation": "Unavailable", "crop": "Maize"},
    "F4": {"soil": "Wet", "irrigation": "Unavailable", "crop": "Rice"}
}

print("\nTASK 1")

print("""
Dry(F1)
IrrigationAvailable(F1)
Rice(F1)

Wet(F2)
IrrigationAvailable(F2)
Wheat(F2)

Dry(F3)
IrrigationUnavailable(F3)
Maize(F3)

Wet(F4)
IrrigationUnavailable(F4)
Rice(F4)
""")

print("PREDICATE RULES")
print("1. Dry(x) AND IrrigationAvailable(x) -> NeedsWater(x)")
print("2. NeedsWater(x) -> Irrigate(x)")
print("3. Wet(x) -> NOT NeedsWater(x)")
print("4. IrrigationUnavailable(x) -> NOT Irrigate(x)")
print("5. Rice(x) AND NeedsWater(x) -> PriorityIrrigation(x)")

print("\nTASK 2")

if fields["F1"]["soil"] == "Dry" and fields["F1"]["irrigation"] == "Available":
    print("F1 -> Needs Water -> Irrigate")
else:
    print("F1 -> Do Not Irrigate")

if fields["F2"]["soil"] == "Dry" and fields["F2"]["irrigation"] == "Available":
    print("F2 -> Needs Water -> Irrigate")
else:
    print("F2 -> Do Not Irrigate")

if fields["F3"]["soil"] == "Dry" and fields["F3"]["irrigation"] == "Available":
    print("F3 -> Needs Water -> Irrigate")
else:
    print("F3 -> Cannot Irrigate")

if fields["F4"]["soil"] == "Dry" and fields["F4"]["irrigation"] == "Available":
    print("F4 -> Needs Water -> Irrigate")
else:
    print("F4 -> Do Not Irrigate")

print("\nTASK 3")
print("""
F1 and F3 are both dry.

F1 has irrigation available, so it can be irrigated.

F3 has irrigation unavailable, so it cannot be irrigated.

Therefore, F1 and F3 must be treated differently.
""")

print("TASK 4")
print("""
Predicate logic alone is not always sufficient because sensor
information can be incomplete, noisy, uncertain or conflicting.

It can be combined with:
1. Fuzzy Logic
2. Probability
3. Machine Learning
4. Sensor Fusion
""")

print("=" * 60)
print("AGRICULTURE ANALYSIS COMPLETED")
print("=" * 60)
