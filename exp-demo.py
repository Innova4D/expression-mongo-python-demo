# exp-demo.py
# Author: Francisco Gutierrez
# Date: September 20, 2015

# A tiny script in Python to:
# 1) Connect to a Meteor - MongoDB document collection
# 2) Insert demo documents

from pymongo import MongoClient

# connect to the MongoDB on MongoLab
# to learn more about MongoLab visit http://www.mongolab.com
# replace the "" in the line below with your MongoLab connection string
# you can also use a local MongoDB instance
connection = MongoClient("localhost:3001/meteor")

# insert the record
db.topics.insert('{ name : "Francisco", isActive : 1, creator : "Twitter", timestamp : ISODate("2015-07-07T16:03:40.838Z"), avgSen : 0.45081967213114754, total : 252, bars : { excellent : 72, good : 68, neutral : 13, bad : 92, terrible : 7	}, keywords : { Guerrero : 22, crimen : 18, ayudemos : 16, red : 6, rat : 5 }}');
# find all documents
results = db.find()

print()
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-')

# display documents from collection
#for record in results:
# print out the document
#print(record['name'] + ',',record['grade'])
print()
# close the connection to MongoDB
connection.close()
