from openai import OpenAI

client = OpenAI()

prompt = "Write a short paragraph about Artificial Intelligence."

response = client.responses.create(
    model="gpt-5.6",
    input=prompt
)

print("Generated Text:")
print(response.output_text)
