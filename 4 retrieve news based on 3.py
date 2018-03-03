# to extract news based on the words extracted previously

import json
import newsapi
from newsapi import NewsApiClient
import pymongo
from pymongo import MongoClient

# connecting to database using pymongo

client = MongoClient()
db = client.dbasenews
ncollec = db.ncollec

# authorization for the news client

newsapi = NewsApiClient(api_key='77a15f1c760b48799bb2186f0c5fd142')

# opening necessary files

source = open('TextsExtracted.txt', 'r')
destination = open('NewsExtracted.txt', "w")

# for each word in the text file, we retrieve a single news article based on relevancy and store it in a file and in a database

for word in source:
	all_articles = newsapi.get_everything(q=word, language='en', from_parameter="2018-03-01", sort_by="relevancy", page_size=1)
	print(all_articles)
	json.dump(all_articles, destination)
	destination.write("\n")
	try:
		ncollec.insert(all_articles)
	except:
		pass

# works for only first 1000 words.. beyond that.. paid plan is necessary
