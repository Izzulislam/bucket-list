from pymongo import MongoClient

client = MongoClient('mongodb+srv://izzul:sparta@cluster0.k3ll4ye.mongodb.net/?retryWrites=true&w=majority')

db = client.dbsparta

doc1 = { 'name' : 'izul','age' : 23 }
doc2 = { 'name' : 'anto','age' : 22 }
doc3 = { 'name' : 'nadia','age' : 21 }

db.users.insert_one(doc1)
db.users.insert_one(doc2)
db.users.insert_one(doc3)