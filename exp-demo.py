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

##### How many sentiment cards?
sc = 2
##### How many comments/second?
cmts = 10
#### Probability of succesful comment
acc  = 100
#### Text for comments and words.
txt = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat mas"
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
    topics.insert({ "name" : "Demo Card " + str(i) , "isActive" : 1, "creator" : "Twitter", "timestamp": datetime.datetime.utcnow(), "avgSen" : 0, "total" : 0, "bars" : { "excellent" : 0, "good" : 0, "neutral" : 0, "bad" : 0, "terrible" : 0}, "keywords" : { "Guerrero" : 0, "crimen" : 0, "ayudemos" : 0, "red" : 0, "rat" : 0 }});

# find all the topics to get the ID.
results = topics.find()
print('Cards created...')

def performQuery():
    for record in topics.find():
        comments.insert({"topic": record['_id'], "author": "", "posted": datetime.datetime.utcnow(), "loc": {"lng": 98.91, "lat": 110.23}, "sentiment":2, "keywords": ["bonito", "hermoso"], "text": "El cielo es bonito y muy hermoso"})
        print('comment::' + record["name"])
    time.sleep(1)

while True:
    performQuery()
