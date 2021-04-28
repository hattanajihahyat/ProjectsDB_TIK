import pymongo

print(" Program Demo Operasi CRUD MongoDB Loop Database  ")
print("                 Hatta Najih Ahyat                ")
print("                 19/447309/SV/17003               ")
print("                        ARM 1                     ")
print("================================================\n")
print("Menu Operasi Database")
print("1. Create Collection ")
print("2. Insert data")
print("3. Select/search data")
print("4. Update data")
print("5. Delete data")
menu=input("Silahkan pilih operasi ( 1 / 2 / 3 / 4 / 5 ) = ")
print("Operasi Yang Anda Pilih = " + menu)

if menu=='1' :
    print("Create Collection")
    #create database
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["user"]
    print(myclient.list_database_names())
    #create collection
    mycol = mydb["customers"]
    print(mydb.list_collection_names())
    mylist = [
    { "_id": 1, "name": "bambang", "address": "gang pete"},
    { "_id": 2, "name": "joko", "address": "gang jambu"},
    ]
    x = mycol.insert_many(mylist)
    #print list of the _id values of the inserted documents:
    print(x.inserted_ids)
    for x in col.find():
        print(x)

elif menu=='2':
    print("Insert data")
    #insert data
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["user"]
    mycol = mydb["customers"]
    mydict = { "_id":3, "name": "jali", "address": "gang jengkol" }
    x = mycol.insert_one(mydict)

elif menu=='3':
    print("Select/search data")
    #select data
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["user"]
    mycol = mydb["customers"]

    myquery = { "address": "gang jambu" }

    mydoc = mycol.find(myquery)

    for x in mydoc:
     print(x)
elif menu=='4':
    ("Update data")
    #update data
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["user"]
    mycol = mydb["customers"]
    myquery = { "address": "gang jengkol" }
    newvalues = { "$set": { "address": "gang tomat" } }
    mycol.update_one(myquery, newvalues)
    #print "customers" after the update:
    for x in mycol.find():
        print(x)

elif menu=='5':
    print("Delete data")
    #delete data
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["user"]
    mycol = mydb["customers"]

    myquery = { "address": "gang tomat" }

    mycol.delete_one(myquery)

    lagi=input("\nTry again (Y/y) ? ")
    if lagi.lower() == "y" :
        main ()
    else :
        print("Program has done")
    
main() 