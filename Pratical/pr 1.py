import re

text = "Anil and Arun are learning Artificial Intelligence."

match = re.search(r"\bArun\b", text)

if match:
    print("Pattern found:", match.group())
else:
    print("Pattern not found")

words = re.findall(r"\bA\w*", text)

print("Words starting with A:", words)
