
def generate_plural(noun):

    if noun.endswith(("s", "x", "z", "ch", "sh")):
        plural = noun + "es"

    elif noun.endswith("y") and noun[-2].lower() not in "aeiou":
        plural = noun[:-1] + "ies"

    else:
        plural = noun + "s"

    return plural
 
words = ["cat", "bus", "box", "baby", "toy", "book"]

print("Singular\tPlural")
print("----------------------")

for word in words:
    print(f"{word:10}\t{generate_plural(word)}")
