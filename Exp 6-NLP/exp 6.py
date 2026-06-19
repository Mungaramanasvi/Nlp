import random

text = "I love python and I love programming"

words = text.split()

bigrams = {}

for i in range(len(words)-1):
    key = words[i]

    if key not in bigrams:
        bigrams[key] = []

    bigrams[key].append(words[i+1])


word = "I"

output = word

for i in range(5):
    next_word = random.choice(bigrams[word])
    output += " " + next_word
    word = next_word

print(output)
