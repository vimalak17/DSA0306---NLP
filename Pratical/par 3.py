import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()

text = "Students are studying Python and birds are flying."

words = text.replace(".", "").split()

print("Word\t\tLemma")
print("----------------------")

for word in words:
    print(f"{word:12}{lemmatizer.lemmatize(word)}")
