from pymongo import MongoClient

client = MongoClient('mongodb+srv://izzul:sparta@cluster0.k3ll4ye.mongodb.net/?retryWrites=true&w=majority')

db = client.dbsparta

doc = {
    'name' : 'izul',
    'age' : 22
}

db.users.insert_one(doc)