import nltk
from nltk.wsd import lesk
from nltk.corpus import wordnet
nltk.download('wordnet')
nltk.download('omw-1.4')
sentence="i went to the bank to deposit money"
words=sentence.split()
result=lesk(words,"bank")
print("sentence:",sentence)
print("Ambiguous word:bank")
if result:
    print("selected sense:", result.name())
    print("Definition:",result.definition())
else:
    print("No sense found")
