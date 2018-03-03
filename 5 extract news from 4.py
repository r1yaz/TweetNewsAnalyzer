# to extract the news text only from the news articles

import pymongo
from pymongo import MongoClient
import json

# connecting to database using pymongo

client = MongoClient()
db = client.dbasenews
ncollec = db.ncollec

# defining a query parameter

elem = {'$match': {'status': 'ok', 'articles.title': {'$exists': 'True'}, 'articles.description': {'$exists': 'True'}}}

# opening file to write to

save = open("NewsExtractedText.txt", "w")

# looping through database and extracting text only from the database

for item in db.ncollec.aggregate([elem, {'$unwind': '$articles'}, elem]):
	print(item['articles']['title'])
	print("\n")
	print(item['articles']['description'])
	print("------------------------------------------------------------------------------------------------")
	json.dump(item['articles']['description'], save)
	save.write("\n")

# replacing the "text:" with emtpy space for futher improvements

with open('Texts.txt', 'r') as file:
	filedata = file.read()

filedata = filedata.replace('{"text": ', '')
file.close()
with open('Texts.txt', 'w') as file:
	file.write(filedata)

save.close()  # closing the savefile to avoid problems
