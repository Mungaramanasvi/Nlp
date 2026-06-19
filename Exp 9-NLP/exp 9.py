import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import RegexpTagger

text = "Ravi is running quickly"

words = word_tokenize(text)

patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ly$', 'RB'),
    (r'.*', 'NN')
]

tagger = RegexpTagger(patterns)

print(tagger.tag(words))
