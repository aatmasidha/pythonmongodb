import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

print("\n\t\t Delete Address Mountain 21")
myquery = { "address": "Mountain 21" }
mycol.delete_one(myquery)


print("Delete address: {$regex: ^S}")
myquery = { "address": {"$regex": "^S"} }
x = mycol.delete_many(myquery)

print(x.deleted_count, " documents deleted.")


print("Delete All")
x = mycol.delete_many({})

print("Drop collection")
mycol.drop()
print(x.deleted_count, " documents deleted.")