from nltk.tokenize import word_tokenize

text = "Cats are running"

words = word_tokenize(text)

tags = []

for word in words:
    if word.endswith("ing"):
        tags.append((word, "VBG"))
    elif word.lower() in ["is", "are", "am"]:
        tags.append((word, "VB"))
    else:
        tags.append((word, "NN"))

print(tags)
