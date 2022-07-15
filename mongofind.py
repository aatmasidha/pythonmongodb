import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

print("\n\t\t find one")
x = mycol.find_one()

print(x)

print("\n\t\t find all")
for x in mycol.find():
  print(x)
  
# Hide id column and show address and name column
print("\n\t\t _id: 0, name: 1, address: 1")
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print("_id, name, address", x )
  
# Hide id column and show address
print("\n\t\t address 0")
for x in mycol.find({},{ "address": 0 }):
  print("Address 0",x)
  
# Both conditions are contradicting so gives error.
# for x in mycol.find({},{ "name": 0, "address": 1 }):
#   print(x)
print("\n\t\t address Park Lane 38 ")  
myquery = { "address": "Park Lane 38" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
 

print("\n\t\t { $gt: S } ")  
myquery = { "address": { "$gt": "S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)


print("\n\t\t address: { $regex: ^S }")   
myquery = { "address": { "$regex": "^S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
  
print("\n\t\t Sort By Name")   
mydoc = mycol.find().sort("name")

for x in mydoc:
  print(x)
  
print("\n\t\t Sort By Name Descending") 
mydoc = mycol.find().sort("name", -1)

for x in mydoc:
  print(x)
  