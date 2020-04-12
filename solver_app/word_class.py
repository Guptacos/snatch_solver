from collections import Counter
from nltk.stem.snowball import SnowballStemmer

class LibWord():

    def __init__(self, word):
        self.text = word
        self.len = len(word)
        self.count = Counter(word)

        stemmer = SnowballStemmer('english')
        self.root = stemmer.stem(word)

    # For each letter in self, other has at least as many of that letter
    def isSubsetOf(self, other):
       return all(other.count.get(k, 0) >= v for k, v in self.count.items())

    def differentRootFrom(self, other):
        return self.root != other.root

    # Convenience function mirrors differentRootFrom for client code readability
    def sameRootAs(self, other):
        return self.root == other.root

    # Used for debugging
    def __repr__(self):
        return 'word: ' + self.word + ', root: ' + self.root

    # Human readable
    def __str__(self):
        return self.word
