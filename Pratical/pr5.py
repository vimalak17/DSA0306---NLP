from collections import defaultdict
import random
  
text = "Machine learning improves data analysis and machine learning creates smart applications"
 
words = text.split()
 
bigram = defaultdict(list)

for i in range(len(words) - 1):
    bigram[words[i]].append(words[i + 1])
 
word = "Machine"
print("Generated Text:")

print(word, end=" ")

for i in range(10):
    if word in bigram:
        word = random.choice(bigram[word])
        print(word, end=" ")
    else:
        break
