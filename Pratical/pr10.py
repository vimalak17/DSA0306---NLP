
sentence = "The dog can bark loudly"

 
words = sentence.split()
 
tags = []

for word in words:
    tags.append([word, "NN"])
 
for i in range(len(tags)):

    word = tags[i][0].lower()

  
    if word in ["the", "a", "an"]:
        tags[i][1] = "DT"

   
    elif word == "can":
        tags[i][1] = "MD"
 
    elif i > 0 and tags[i-1][1] == "MD":
        tags[i][1] = "VB"
 
    elif word.endswith("ly"):
        tags[i][1] = "RB"
 
print("Sentence:")
print(sentence)

print("\nTransformation-Based POS Tags:")

for word, tag in tags:
    print(word, "->", tag)
