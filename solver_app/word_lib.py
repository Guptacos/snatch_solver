from solver_app.word_class import LibWord

dictionaryFile = '/app/solver_app/english_dictionary.txt'

# @return: a dict of lists of LibWord objects constructed from the dict file.
#          The dict contains lists of words, where the key is the number of
#          letters in all words in the list.
#
# I.e. result[4] contains all 4 letter words in the dictionary, represented as
# LibWord() objects.
def getDict():
    result = dict()
    with open(dictionaryFile, 'r') as f:
        for cnt, word in enumerate(f):
            # Remove new line
            if word[-1] == '\n':
                word = word[:-1]

            # Initialize list if len not in dict
            wordLen = len(word)
            if wordLen not in result:
                result[wordLen] = []

            result[wordLen].append(LibWord(word))
    return result

# @param wordDict: the dict created by getDict. Pass in instead of recomputing.
# @param word: the word you're trying to steal.
# @param length: the max length of new words to look for.
# @note: longest word in the english language is ~46 characters?
#        I have never seen a word longer than ~10-12 in snatch
# @note: this function is basically cheating, and shouldn't be used except for
#        an AI or a hint giving system. Or cheating, if you're into that.
def getPossibleSteals(wordDict, word, maxLen=20):
    ogWord = LibWord(word)
    result = []

    for elemLen, wordList in wordDict.items():
        # Skip words that are too long or short
        if elemLen > maxLen or elemLen <= ogWord.len:
            continue

        for dictWord in wordList:
            if dictWord.sameRootAs(ogWord):
                continue

            if ogWord.isSubsetOf(dictWord):
                result.append(dictWord.text)

    result.sort(key=len)
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

# @param ogWord: a string containing the original word
# @param letter: a character, returns what permutations of ogWord + letter are
#                new words
# @return set of new words that can be made, empty if none can be made
'''
def newWords(ogWord, letter):
    dictionary = getDict()

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
'''

# Equivalent to newWords, but considers combinations of multiple letters
#
# @param word: the word being stolen
# @param letters: the letters available in the middle of the board as a string
# @return a set containing every word that can be made
'''
def newWordsManyLetters(wordDict, word, letters):
    maxLen = len(word) + len(letters)
    possibleSteals = getPossibleSteals(wordDict, word, maxLen)

    permutations = permute(letters)

    result = []
    for elem in permutations:
        if
        result = result.union(newWords(word, elem))

    return result
'''
