dialogue = [
    ("User", "I want to book a flight."),
    ("Agent", "Where would you like to travel?"),
    ("User", "I want to go to Delhi."),
    ("Agent", "From which city?"),
    ("User", "From Chennai.")
]

state = {
    "Departure City": None,
    "Destination City": None,
    "Travel Date": None,
    "Number of Passengers": None
}

def update_state(text):
    text_lower = text.lower()

    if "delhi" in text_lower:
        state["Destination City"] = "Delhi"

    if "chennai" in text_lower:
        state["Departure City"] = "Chennai"

def get_missing_slot():
    for slot, value in state.items():
        if value is None:
            return slot
    return None

for speaker, utterance in dialogue:
    if speaker == "User":
        update_state(utterance)

    print(speaker, ":", utterance)
    print("Current State:", state)

print("\nFINAL DIALOGUE STATE")

for slot, value in state.items():
    print(slot, ":", value)

missing = get_missing_slot()

print("\nNext Question:")

if missing == "Travel Date":
    print("What is your travel date?")
elif missing == "Number of Passengers":
    print("How many passengers are travelling?")
elif missing:
    print("Please provide your", missing)
else:
    print("All required information has been collected.")
