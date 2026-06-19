import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Download required packages
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

# Input text
text = "The cat sits on the mat"

# Tokenization
words = word_tokenize(text)

# POS Tagging
tags = pos_tag(words)

# Display output
print(tags)
