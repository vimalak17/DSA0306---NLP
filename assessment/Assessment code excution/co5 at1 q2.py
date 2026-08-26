conversation = [
    "I submitted my assignment, but I am worried that I may have made many mistakes."
]

def identify_dialog_act(text):
    text = text.lower()

    if "worried" in text or "mistakes" in text:
        return ["Reassure", "Advise"]

    return ["Inform"]

def identify_entities(text):
    entities = []

    if "assignment" in text.lower():
        entities.append("assignment")

    if "mistakes" in text.lower():
        entities.append("mistakes")

    if "i" in text.lower():
        entities.append("you")

    return entities

text = conversation[0]

acts = identify_dialog_act(text)
entities = identify_entities(text)

responses = [
    "Don't worry; it is normal to feel concerned about mistakes after submitting an assignment. You can review the feedback carefully and use it to improve your work, which will help you feel more confident next time.",
    "It is okay to be worried, but submitting your assignment is already an important achievement. Review any feedback you receive and use it to improve your understanding, so you can feel more confident about your future assignments.",
    "You do not need to worry too much about the mistakes because they can become opportunities to learn. Review your assignment feedback carefully and use it to improve your work and become more confident."
]

print("DIALOG ACTS")
print("-" * 40)

for act in acts:
    print(act)

print("\nIMPORTANT ENTITIES")
print("-" * 40)

for entity in entities:
    print(entity)

print("\nPOSSIBLE RESPONSES")
print("-" * 40)

for i, response in enumerate(responses, 1):
    print("\nResponse", i)
    print(response)

print("\nBEST RESPONSE")
print("-" * 40)

print(responses[0])
