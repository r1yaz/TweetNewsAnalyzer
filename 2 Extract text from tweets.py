# To extract the texts portion from the database present in mongodb and store in a text file
import pymongo
from pymongo import MongoClient
import json

# initialising mongoclient from pymongo

client = MongoClient()
db = client.dbase
tcollec = db.tcollec

savefile = open('Texts.txt', "w")
'''
open savefile as a text file to which we are going to extract the 'text' section of a tweet 
which is stored in the mongodb instance 
'''
for i in db.tcollec.find({'lang': "en"}, {"text": 1, "_id": 0}):  # looping through each json document and enabling text parameter and disabling _id parameter
	json.dump(i, savefile)  # dumping the contents of i in savefile
	savefile.write("\n")  # newline for convenience purposes
	print(i)

savefile.close()  # closing the savefile to avoid problems
