from socialnetwork.word_class import LibWord

dictionaryFile = '/app/socialnetwork/english_dictionary.txt'

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
