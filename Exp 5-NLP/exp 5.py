from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["playing", "running", "studies"]

for word in words:
    print(word, "->", ps.stem(word))
