
#For MONGO Python connector for python version 3.10.0 the pymongo version should be 3.12.0
import pymongo

def connectToDatabase():
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient['mydatabase']
    print("mydb:", mydb)

    
    print(myclient.list_database_names())
    
    dblist = myclient.list_database_names()
    if "mydatabase" in dblist:
        print("The database exists.")
        
    mycol = mydb["customers"]
    print(mydb.list_collection_names())
    
    collist = mydb.list_collection_names()
    if "customers" in collist:
        print("The collection exists.")
    
    mydict = { "name": "John", "address": "Highway 37" }

    x = mycol.insert_one(mydict)
    mydict = { "name": "Peter", "address": "Lowstreet 27" }
    x = mycol.insert_one(mydict)
    print(x.inserted_id)
    
    

if __name__ == "__main__":
    print("Inside Main()")
    connectToDatabase()