import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V
Det -> 'The'
N -> 'boy'
V -> 'runs'
""")

parser = nltk.ChartParser(grammar)

sentence = "The boy runs".split()

for tree in parser.parse(sentence):
    tree.pretty_print()
