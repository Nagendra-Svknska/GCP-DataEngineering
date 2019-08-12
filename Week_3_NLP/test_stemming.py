from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

example_words = ["python","pythoner","pythoning","pythoned","pythonly"]
ps=PorterStemmer()

for i in example_words:
    print(ps.stem(i))
