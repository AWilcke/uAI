import re
from HTMLParser import HTMLParser
parser = HTMLParser()

#reads fb data and splits it into messages
def getHtml(filename):
    inpt = open(filename + '.htm', 'r')
    html = inpt.read()
    html = html.split('</p>')
    inpt.close()
    return html

#returns a list of tuples, (User, Message) for use with getResponses
def getMessages(html):
    output = []
    for msg in html:
        #pattern match all messages, grouping user and actual message
        match = re.search('.*<span class="user">(.*)</span><span.*((?<=<p>)..*)', msg)
        if match:
            output.append((parser.unescape(unicode(match.group(1), 'utf-8')), parser.unescape(unicode(match.group(2), 'utf-8'))))
    return output

#returns a list of messages by user
def getUser(html, user):
    output = []
    for msg in html:
        #patten match the desired user and any non-empty message
        match = re.search('.*<span class="user">' + user + '</span>.*((?<=<p>)..*)', msg)
        if match:
            #convert to unicode and parse out special chars
            output.append(parser.unescape(unicode(match.group(1), 'utf-8')))
    return output

#returns corpus of all messages by user
def getCorpus(html, user):
    messages = getUser(html, user)
    output = ''
    for msg in messages:
        output += msg + '\\ '
    return output

#for testing

#h = getHtml('arthur')
#m = getMessages(h)
#u = getUser(h, 'Arthur Wilcke')
#c = getCorpus(h, 'Arthur Wilcke')
