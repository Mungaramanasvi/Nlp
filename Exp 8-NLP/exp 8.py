from nltk.tokenize import word_tokenize

# Simple probabilistic dictionary
prob_tags = {
    "book": "NN",
    "run": "VB",
    "dog": "NN",
    "eats": "VB",
    "cat": "NN"
}

text = "dog eats"
words = word_tokenize(text)

for word in words:
    tag = prob_tags.get(word, "NN")
    print(word, "->", tag)
