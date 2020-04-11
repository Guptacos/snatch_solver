from nltk.stem.snowball import SnowballStemmer
import os
from collections import Counter

dictionaryFile = 'socialnetwork/english_dictionary.txt'

# Returns a set containing the dictionary
def getWords():
    result = set()
    with open(dictionaryFile, 'r') as f:
        for cnt, word in enumerate(f):
            result.add(word[:-1])
    return result
        
# Check if two words are fundamentally different
def differentRoot(w1, w2):
    stemmer = SnowballStemmer('english')
    return stemmer.stem(w1) != stemmer.stem(w2)
    
# @param ogWord: a string containing the original word
# @param letter: a character, returns what permutations of ogWord + letter are
#                new words
# @return set of new words that can be made, empty if none can be made
def newWords(ogWord, letter):
    dictionary = getWords()

    # Count letters in original word
    ogWordCount = Counter(ogWord + letter)
    stealable = set()
    for dictWord in dictionary:
        # Count letters in dict word. If same as original, add to result
        if ogWordCount == Counter(dictWord):
            stealable.add(dictWord)

    # Check which of the new words have a different
    result = set()
    for newWord in stealable:
        if differentRoot(newWord, ogWord):
            result.add(newWord)

    return result

# @param letters: a string to permute
# @return: a list of strings, containing every permutation of the input (order
#          independent)
#          eg: input aba, output [a, b, aa, ab, aab]
# @note: this is bad and inneficient. I don't expect inputs > 5, so largest
#        result size = 2^5 = 32, max recursion depth = 5
def permute(letters):
    if letters is None or len(letters) == 0:
        return []

    if len(letters) == 1:
        return [letters]

    first = letters[0]
    rest = permute(letters[1:])

    result = []
    for elem in rest:
        result += [elem]
        result += [elem + first]

    result += [first]
        
    return result

# Equivalent to newWords, but considers combinations of multiple letters
#
# @param word: the word being stolen
# @param letters: the letters available in the middle of the board
# @return a set containing every word that can be made
def newWordsManyLetters(word, letters):
    permutations = permute(letters)
    result = set()
    for elem in permutations:
        result = result.union(newWords(word, elem))

    return result

# @param word: the word you're trying to steal
# @param length: the max length of new words to look for
# @note: longest word in the english language is ~46 characters?
#        I have never seen a word longer than ~10 in snatch
# @note: this function is basically cheating, and shouldn't be used except for
#        an AI or a hint giving system. Or cheating, if you're into that.
def getPossibleSteals(word, length=20):
    wordCounter = Counter(word)
    result = []

    for dictWord in getWords():
        # Ignore words that are too long or too short
        if len(dictWord) > length or len(dictWord) <= len(word):
            continue
        
        # Ignore words with the same root
        if not differentRoot(dictWord, word):
            continue
        
        # If word is a subset of dictWord
        if all(Counter(dictWord).get(key, None) == val for key, val in wordCounter.items()):
            result += [dictWord]

    result.sort(key=len)
    return result
