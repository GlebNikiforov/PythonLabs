def GetWordList():
    return [str(word) for word in input("Enter word list: ").split(', ')]

def WordListToSet(wordList):
    wordSet = set(wordList)
    wordSetLength = len(wordSet)
    print("This word set cotains {0} word(s).".format(wordSetLength))
    return wordSet

def GetValueList(length):
    print("Enter value list with {0} elements: ".format(length))
    valueList = list()
    for i in range(0, length, 1):
        valueList.append(input("Enter {0}-th value: ".format(i)))
    return valueList

def CreateDictionary(words, values):
    dictionary = {}
    for word, value in zip(words, values):
        dictionary.setdefault(word, value)
    return dictionary

def main():
    wordList = GetWordList()
    wordSet = WordListToSet(wordList)
    valueList = GetValueList(len(wordSet))
    createdDictionary = CreateDictionary(wordSet, valueList)
    print("Created dictionary: {0}".format(createdDictionary))

main()