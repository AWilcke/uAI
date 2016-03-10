from seedgenerator import *

#to be called on bot start, returns bigrams, weightings
def botStart(filename, user):
    html = getHtml(filename)
    corpus = getCorpus(html, user)
    messages = getMessages(html)
    return getBigrams(corpus), getTrigrams(corpus), getResponses(messages, user)

#generate sentence from query
def genSentence(query, weightings, bigrams, trigrams):
    seed = getSeedWord(query, weightings)
    sentence = recurseSentence(bigrams, trigrams, seed)
    return sentence

#generate sentence from word
def recurseSentence(bigrams, trigrams, word):
    if word[-1] == "\\":
        return word[:-1]
    else:
        nextWord = randomChooser(getFollow(bigrams, trigrams, word)).split()[-1]
        #in case it's a trigram, nextWord should still only be one word
        return word + " " + recurseSentence(bigrams, trigrams, nextWord)
    
def dialogue(filename, user):
    print "Generating bot..."
    bigrams, trigrams, weight = botStart(filename, user)
    print "You are now talking to a bot"
    while True:
        query = raw_input()
        print genSentence(query, weight, bigrams, trigrams)
