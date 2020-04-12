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

    # Return letters required to convert one word into the other, as a string
    # Requires either self.isSubsetOf(other) or other.isSubsetOf(self)
    def letterDiff(self, other):
        diff = dict()
        if self.len > other.len:
            diff = self.count - other.count
        else:
            diff = other.count - self.count

        result = ''
        for k,v in diff.items():
            result += k*v

        return ''.join(sorted(result))

    # Used for debugging
    def __repr__(self):
        return 'word: ' + self.text + ', root: ' + self.root

    # Human readable
    def __str__(self):
        return self.text
