def recognize_dialog_act(sentence):
    text = sentence.lower().strip()

    if any(word in text for word in ["hello", "hi", "hey", "good morning"]):
        return "Greeting"

    if "thank" in text or "thanks" in text:
        return "Thanking"

    if any(word in text for word in ["bye", "goodbye", "see you"]):
        return "Goodbye"

    if text.endswith("?"):
        return "Question"

    if any(word in text for word in [
        "please", "could you", "would you", "can you"
    ]):
        return "Request"

    if any(word in text for word in [
        "yes", "no", "correct", "okay", "sure"
    ]):
        return "Answer/Confirmation"

    return "Statement"


dialog = [
    "Hello!",
    "How are you?",
    "I am fine.",
    "Can you help me?",
    "Yes, sure.",
    "Thank you!",
    "Goodbye!"
]

print("Dialog Act Recognition\n")

for sentence in dialog:
    act = recognize_dialog_act(sentence)
    print(f"Sentence: {sentence}")
    print(f"Dialog Act: {act}")
    print()
