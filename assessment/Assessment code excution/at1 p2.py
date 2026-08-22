import re

text = """Artificial Intelligence (AI) is transforming industries across the world.
AI is used in healthcare to assist doctors in diagnosis, in banking to detect fraud,
and in education to provide personalized learning experiences.
Many companies invest heavily in AI research because AI improves efficiency
and enables intelligent decision-making.
As AI continues to evolve, professionals with AI skills are in high demand."""

match = re.search(r"\bAI\b", text)

if match:
    print("First occurrence of AI found")
    print("Starting Position:", match.start())
    print("Ending Position:", match.end())

    count = len(re.findall(r"\bAI\b", text))
    print("Total Number of Occurrences:", count)
else:
    print("The word AI was not found")
