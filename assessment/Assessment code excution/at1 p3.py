import re

# Given passage
text = """Artificial Intelligence (AI) is transforming industries across the world. 
AI is used in healthcare to assist doctors in diagnosis, in banking to detect fraud, 
and in education to provide personalized learning experiences. 
Many companies invest heavily in AI research because AI improves efficiency and enables intelligent decision-making. 
As AI continues to evolve, professionals with AI skills are in high demand."""

# Split into sentences using ., ?, !
sentences = re.split(r'[.!?]+', text)

# Remove empty strings
sentences = [s.strip() for s in sentences if s.strip()]

print("Sentences:")
for s in sentences:
    print(s)

print("\nTotal Number of Sentences:", len(sentences))

# Split into words using one or more whitespace characters
words = re.split(r'\s+', text.strip())

print("\nWords:")
print(words)

print("\nTotal Number of Words:", len(words))
