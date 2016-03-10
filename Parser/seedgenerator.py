from predict import *

#generates a seed word given input-reply weightings
def getSeedWord(input, weightings):
    seedDict = createWeightTable(input, weightings)
    seedWord = randomChooser(convertToAbomination(seedDict))
    return seedWord

#Start conditions are wrong because fucking dictionaries
def getMaxWord(seedDict):
    maxWeight = 0.0
    maxWord = ""
    for word in seedDict:
        if seedDict[word] > maxWeight:
            maxWeight = seedDict[word]
            maxWord = word
    return maxWord

#Creates a dictionary which gives the weights of the reply words based on
#the corresponding weights of every single word in the input
def createWeightTable(input, weightings):
    seedDict = {}
    words = input.split()
    for word in words:
        for item in weightings[word]:
            seedDict[item] = weightings[word][item]
    return seedDict

#Turns my beautiful creation into Arthur's abomination (more specifically
#converts the seed dictionary I create into a format that can be used by
#Arthur's random selection algorithm)
def convertToAbomination(seedDict):
    artDict = {}
    for tup in seedDict.items():
        if artDict.has_key(tup[1]):
            artDict[tup[1]].append(tup[0]) 
        else:
            artDict[tup[1]] = [tup[0]]
    return artDict
