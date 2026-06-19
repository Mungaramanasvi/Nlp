import nltk
from nltk.tokenize import word_tokenize

text = "The boys are playing"

words = word_tokenize(text)

for word in words:
    print(word)
