from newsapi import NewsApiClient
import json
# Init
newsapi = NewsApiClient(api_key='b1070364cb8b47a5b1fef8bbdc1f8662')

# /v2/top-headlines
top_headlines={}

for num in range(1,6):
	top_headlines.update(newsapi.get_everything(q='canada OR university OR dalhousie university OR halifax OR canada education',
		language='en',page=num))

data=[]
count=0

for tweet in top_headlines['articles']:
	data.append({'Source':tweet['source']['name'],'Author':tweet['author'],'Title':tweet['title'],'Content':tweet['content'],
	'Published At':tweet['publishedAt']})

with open('news.json', 'w') as fp:
	json.dump(data, fp, indent=2, sort_keys=True)
