# To collect tweets and store in a mongodb instance using pymongo

import tweepy
import pymongo
from pymongo import MongoClient
import json
import sys

# defining authorization keys

consumer_key = "DuTnIVycQk19LOn1IHYo0KwoT"  # defining the consumer key
consumer_secret = "C3NgRYPNxoAM9ZEpg9tiL7gKH50p2zeKQF1W2ENgvzc64oD5HI"  # defining the consumer secret
access_token = "964857091520266241-mwN2JgcHIrTzEC1Unjf28ioztkavzLt"  # defining the access token
access_token_secret = "oOkQF4ahUHxiHq4HuIpBDX5cIYPHq9zQFJGhAhsPhX8ie"  # defining the access token secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  # creating an OauthHandler instance and passing parameters
auth.set_access_token(access_token, access_token_secret)  # setting the access tokens for auth
api = tweepy.API(auth)

# initialising mongoclient for connecting to the mongodb database

client = MongoClient()
db = client.dbase
tcollec = db.tcollec
tcollec.create_index([("id", pymongo.ASCENDING)], unique=True)

# defining a class to insert data into mongodb

class MyStreamListener(tweepy.StreamListener):
	def on_status(self, status):
		print(status.id_str)
		count = db.tcollec.count()
		print(count)
		if count == 10000:
			print('please stop the execution')
			sys.exit()

		try:
			tcollec.insert(status._json)
		except:
			pass

	def on_error(self, status_code):
		if status_code == 420:
			return False


# filtering the tweet search using specific parameters

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
while True:
	try:
		myStream.filter(track=["a", "the", "i", "you", "u", "lol", "love"], locations=[-180, -90, 180, 90], async=True, languages=["en"])
	except:
		continue

'''
using the track parameters as a, the, i, you etc.. to fetch most of the queries. 
Location parameter is set to all locations
Language is english
async parameter fetches only unique tweets. 
'''
