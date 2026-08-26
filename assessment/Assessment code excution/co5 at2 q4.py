conversation = [
    ("User", "Hello, I need help with my assignment."),
    ("Agent", "Sure, what problem are you facing?"),
    ("User", "I do not understand machine learning."),
    ("Agent", "I can explain the basic concepts to you.")
]

def classify_utterance(text):
    text_lower = text.lower()

    if text_lower.startswith(("hello", "hi", "hey")):
        return "Greeting"

    if "?" in text:
        return "Question"

    if any(word in text_lower for word in ["need help", "help me", "please"]):
        return "Request"

    if any(word in text_lower for word in ["can explain", "can help", "i can"]):
        return "Offer"

    if text_lower.startswith(("yes", "sure", "okay", "correct")):
        return "Confirmation"

    return "Inform"

print("DIALOGUE ACT CLASSIFICATION")

for speaker, utterance in conversation:
    act = classify_utterance(utterance)
    print(speaker, ":", utterance)
    print("Dialogue Act:", act)
    print()

print("Dialogue Act Sequence:")
print("Greeting -> Request -> Inform -> Offer")
