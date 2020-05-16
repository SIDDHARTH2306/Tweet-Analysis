import json
import csv
from collections import Counter
import pandas as pd

TweetList=[]
TweetSentence=""
with open('tweet.json') as json_file:
    data = json.load(json_file)
    for i in data:
        TweetList.append(i['Tweet'])

BOW=[]

for i in TweetList:
    BOW.append(i.split())

counts=[]

for i in BOW:
    counts.append(dict(Counter(i)))

print(counts)

positive_words=[]
with open('positive-words.txt') as posword:
  positive_words = [pos.strip() for pos in posword.readlines()]

negative_words=[]
with open('negative-words.txt') as negword:
  negative_words = [neg.strip() for  neg in negword.readlines()]

Message=[]
Match=[]
MatchP=[]
MatchN=[]
Positive_Words=[]
Negative_Words=[]
Polarity=[]
pos=0
neg=0

for i in BOW:
    for j in i:
        if j in positive_words:
            pos=pos+1
            MatchP.append(j)
            Positive_Words.append(j)
        if j in negative_words:
            MatchN.append(j)
            Negative_Words.append(j)
            neg=neg+1
    if(pos>neg):
        Polarity.append("Positive")
        Message.append(' '.join(i))
        Match.append(','.join(MatchP))
        MatchP=[]
    elif(neg>pos):
        Polarity.append("Negative")
        Message.append(' '.join(i))
        Match.append(','.join(MatchN))
        MatchN=[]
    elif(pos==neg or pos==0 or neg==0):
        Polarity.append("Neutral")
        Message.append(' '.join(i))
        Match.append("NA")
    else:
        Polarity.append("Neutral")
        Message.append(' '.join(i))
        Match.append("NA")
    pos=0
    neg=0

##df = pd.DataFrame({'Message':Message,'Match':Match,'Polarity':Polarity})
##df.to_csv('Polarity.csv',index=False)
##
##PCount=dict(Counter(Positive_Words))
##NCount=dict(Counter(Negative_Words))
##
##print(PCount)
##print(NCount)
##
##with open('PositiveW.csv', 'w') as f:
##    for key in PCount.keys():
##        f.write("%s, %s\n" % (key, PCount[key]))
##
##with open('NegativeW.csv', 'w') as f:
##    for key in NCount.keys():
##        f.write("%s, %s\n" % (key, NCount[key]))


print("Done")
