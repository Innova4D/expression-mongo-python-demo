# exp-demo.py
# Author: Francisco Gutierrez
# Date: September 20, 2015

# A tiny script in Python to:
# 1) Connect to a Meteor - MongoDB document collection
# 2) Insert demo documents
#
# Note:
# For tests purposes only.
# This Script will DESTROY everything in the meteor database.
# Please backup first.

from pymongo import MongoClient
import datetime
import time
import random

##### How many sentiment cards?
sc = 4
##### How many comments/second?
cmts = 10
#### Probability of succesful comment
acc  = 20

#### Text for comments and words.
txt = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et ma"
# Set the mongoDB location (meteor defaults)
client = MongoClient("localhost", 3001)
#Set the database to "meteor"
db = client.meteor

# --------> Warning! The following line will destroy the meteor DB contents <--------
client.drop_database("meteor");

# pointer the topics collection
topics   = db.topics
comments = db.comments

# create sentiment cards
for i in range(sc):
    topics.insert({ "name" : "Demo Card " + str(i) , "isActive" : 1, "creator" : "Twitter", "timestamp": datetime.datetime.utcnow(), "avgSen" : 0, "total" : 0, "bars" : { "excellent" : 0, "good" : 0, "neutral" : 0, "bad" : 0, "terrible" : 0}, "keywords" : { "lorem" : 0, "ipsum" : 0, "dolor" : 0, "amet" : 0, "sit" : 0 }});

# find all the topics to get the ID.
results = topics.find()
print('Cards created...')

def performQuery():
    for _ in range(cmts):
        for record in topics.find():
            sr = random.randrange(-2, 3)
            if random.randrange(0, 100) <= acc:
                comments.insert({"topic": record['_id'], "author": "", "posted": datetime.datetime.utcnow(), "loc": {"lng": 98.91, "lat": 110.23}, "sentiment":sr, "keywords": ["bonito", "hermoso"], "text": txt})
                topics.update({'_id':record["_id"]}, {"$set": {"total" : record["total"]+1}}, upsert=False)
                if sr == -2: topics.update({'_id':record["_id"]}, {"$set": {"bars.terrible" :  record["bars"]["terrible"]+1}}, upsert=False)
                if sr == -1: topics.update({'_id':record["_id"]}, {"$set": {"bars.bad" :       record["bars"]["bad"]+1}}, upsert=False)
                if sr ==  0: topics.update({'_id':record["_id"]}, {"$set": {"bars.neutral" :   record["bars"]["neutral"]+1}}, upsert=False)
                if sr ==  1: topics.update({'_id':record["_id"]}, {"$set": {"bars.good" :      record["bars"]["good"]+1}}, upsert=False)
                if sr ==  2: topics.update({'_id':record["_id"]}, {"$set": {"bars.excellent" : record["bars"]["excellent"]+1}}, upsert=False)
                print('comment::' + record["name"])
    time.sleep(1)

while True:
    performQuery()
