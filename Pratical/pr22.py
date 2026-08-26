import nltk
from nltk import word_tokenize, pos_tag

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger_eng")

text = "Ravi met Arun at the library. He was looking for a book. Arun helped him find it."

sentences = nltk.sent_tokenize(text)

pronouns = {
    "he": "male",
    "him": "male",
    "his": "male",
    "she": "female",
    "her": "female",
    "hers": "female",
    "it": "neutral",
    "they": "plural",
    "them": "plural",
    "their": "plural"
}

male_names = {"ravi", "arun"}
female_names = {"anita", "meena", "sita"}

previous_nouns = []

for sentence in sentences:
    words = word_tokenize(sentence)
    tagged = pos_tag(words)

    for word, tag in tagged:
        word_lower = word.lower()

        if tag.startswith("NNP"):
            previous_nouns.append(word)

        if word_lower in pronouns:
            antecedent = "Unknown"

            for noun in reversed(previous_nouns):
                noun_lower = noun.lower()

                if pronouns[word_lower] == "male" and noun_lower in male_names:
                    antecedent = noun
                    break

                if pronouns[word_lower] == "female" and noun_lower in female_names:
                    antecedent = noun
                    break

                if pronouns[word_lower] == "neutral":
                    antecedent = noun
                    break

            print(f"Reference: {word}")
            print(f"Possible antecedent: {antecedent}")
            print()
