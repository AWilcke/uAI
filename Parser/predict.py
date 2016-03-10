from parser import *
import nltk
from nltk.collocations import *
from collections import defaultdict
import random

bigram_measures = nltk.collocations.BigramAssocMeasures()

def getBigrams(corpus):
    bigrams = BigramCollocationFinder.from_words(corpus.split())
    #bigrams.apply_freq_filter(2)           #removed because we if we filter we dont have
    return bigrams.ngram_fd.viewitems()     #enough words

def getTrigrams(corpus):
    trigrams = TrigramCollocationFinder.from_words(corpus.split())
    trigrams.apply_freq_filter(2)
    return trigrams.ngram_fd.viewitems()

#functions

#returns the dictionary of possible follow words for a given word
def getFollow(bigrams, trigrams, word):
    output = {}
    #go trough trigrams
    for ((first, second, third), count) in trigrams:
        if first == word:
            try:    #case where key already exists
                output[count].append(second + ' ' + third)
            except: #case where it has to be created
                output[count] = [second + ' ' + third]
    #and trough the bigrams
    for ((first, second), count) in bigrams:
        if first == word:
            try:    
                output[count].append(second)
            except: 
                output[count] = [second]
    return output

#total dictionary of seed words
def getResponses(messages, user):
    responseDict = defaultdict(dict)
    lastSentence = ""
    for msg in messages:
            if msg[0] == user :
                lastWords = lastSentence.split()
                firstWord = msg[1].split()[0]
                for word in lastWords:
                    #responseDict[word][firstWord] +=1
		    try:
			responseDict[word][firstWord] += 1
		    except:
			responseDict[word][firstWord] = 1
            else:
                lastSentence = msg[1]
    return responseDict

def randomChooser(dic):

    numbers = dic.keys()
    total = sum(numbers)                #total probability
    if total == 0:                      #if word has no follow
        return '\\'                     #return sentence end
    rand = random.randint(1,total)      #randomly chose somewhere in the range
    current = 0                         #current point
    index = 0                           #index
    for i in numbers:
        current+=i
        if current>=rand:
            break
        else:
            index+=1
    return dic[numbers[index]][random.randrange(len(dic[numbers[index]]))]
