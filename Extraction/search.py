import tweepy
from keys import *
import os
import tweepy as tw
import re
import json

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_token)
api = tw.API(auth, wait_on_rate_limit=True)


search_words = ['Halifax','Dalhousie University','Canada','Canada Education','University']
# Collect tweets
tweetList=[]

for word in search_words:
	tweets = tw.Cursor(api.search,q=word,lang="en",tweet_mode='extended').items(500)

count=0
data = []

for tweet in tweets:
	text = re.sub(r"http\S+", "", tweet.full_text).encode('ascii', 'ignore').decode('ascii')
	data.append({'Tweet':re.sub('rt [^\\s]+','',text)})

with open('tweet.json', 'w') as fp:
	json.dump(data, fp, indent=2, sort_keys=True)




