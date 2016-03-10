import telepot
import time
from sentencegen import *

bot = telepot.Bot('yourkeyhere')


#load everyone up
aB, aT, aW = botStart('filename','firstname lastname')
print "First bot booted up woohoo"
mB, mT, mW = botStart('filename','firstname lastname')
print "second bot up in this motherfucker"
tB, tT, tW = botStart('filename','firstname lastname')
print "third bot here"

#default
bigrams, trigrams, weight = aB, aT, aW
active = 'first'

def handle_message(msg):
    global active, bigrams, trigrams, weight, aB, aT, aW, mB, mT, mW, tB, tT, tW
    msg_type, chat_type, chat_id = telepot.glance2(msg)
    if msg_type != 'text':
        return
    input = msg['text']
    reply_id = chat_id
    if "/changebot_first" in input and active!='first':
        bigrams, trigrams, weight = aB, aT, aW
        active = 'first'
        print "first loaded"
        bot.sendMessage(reply_id, "first bot here")

    elif "/changebot_second" in input and active!='second':
        bigrams, trigrams, weight = mB, mT, mW
        active = 'second'
        print "second loaded"
        bot.sendMessage(reply_id, "second bot here")

    elif "/changebot_third" in input and active!='third':
        bigrams, trigrams, weight = tB, tT, tW
        active = 'third'
        print "third loaded"
        bot.sendMessage(reply_id, "third bot here")

    else:
        try:
            bot.sendMessage(reply_id, genSentence(input, weight, bigrams, trigrams))
        except:
            bot.sendMessage(reply_id, "U WOT M8?")

bot.notifyOnMessage(handle_message)

# Keep the program running.
while 1:
    time.sleep(10)
