import json

search_words = ['education','halifax','dalhousie','Canada','University','expensive','school','good schools','bad schools','poor school','poor schools','faculty','computer science','graduate']
count=0
ncount=0

with open('results.json') as json_file:
    data = json.load(json_file)

with open('news.json') as json_file1:
    news = json.load(json_file1)

counter=[]
newsCount=[]

for key in search_words:
	for val in data:
		tweet = str(val['Tweet']).lower()
		key = key.lower()
		if key in tweet:
			count=count+1
	counter.append(count)
	count=0

dictT={}

for i in range(len(search_words)):
	dictT.update({search_words[i]:counter[i]})

print(dictT)

###############################################

for key in search_words:
	for val in news:
		tweet = str(val['Content']).lower()
		key = key.lower()
		if key in tweet:
			ncount=ncount+1
	newsCount.append(count)
	ncount=0

newsT={}

for i in range(len(search_words)):
	newsT.update({search_words[i]:newsCount[i]})

print(newsT)

with open('output.txt', 'a') as file:
     file.write(json.dumps(dictT,indent=2, sort_keys=True))

with open('output.txt', 'a') as file:
     file.write(json.dumps(newsT,indent=2, sort_keys=True))