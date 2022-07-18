
import collections
from datetime import datetime
from email import message
from sqlite3 import Date
from bson import BSON
import pymongo
from Random import  randomid_Dvid, random_N_Crt, date_convert


client = pymongo.MongoClient("mongodb+srv://duyvippro09:duy1234@cluster0.cg0vx.mongodb.net/?retryWrites=true&w=majority")
db = client['deviceDB']
def add_message(Message):
    collection_name = db["messageDB"]
    try:
        dateCvt= date_convert()
        messageDay = collection_name.find_one({"message_id":date_convert()})
        print(messageDay)
        
        collection_name.update_one({"message_id":date_convert()},{"$set":{"message_count":messageDay["message_count"]+1}})
        collection_name.update_one({"message_id":date_convert()},{"$push":{"messages":Message}})
        print("update success")
    except:
        message_date={
            
            "message_id":date_convert(),
            "time": datetime.now(),
            "message_count": 1,
            "messages":[]
        }
        collection_name.insert_one(message_date)
        collection_name.update_one({"message_id":date_convert()},{"$push":{"messages":Message}})
def create_device(device_name ):
    collection_name = db["dvData"]
    message ={
        "API": random_N_Crt(12),
        "Time_create": datetime.now(),
        "Device_name": device_name,
        "message_count": 0,
        #"timestamp":BSON(datetime.utcfromtimestamp(7)),
        "datas":[]
    }
    try:
        collection_name.insert_one(message)
        return 1
    except:
        return 0
    
def update_data(apiDevice,data):
    collection_name = db["dvData"]
    device = collection_name.find_one({"API":apiDevice})
    count = 0
    print(device)
    try:
        count = device["message_count"]
        print(count)
        collection_name.update_one({"API":apiDevice},{"$set":{"message_count":count+1}})
        data = {
            "Time": datetime.now(),
            "data": data,
        }
        collection_name.update_one({"API":apiDevice},{"$push":{"datas":data}})
        return count +1
    except:
        print("can't get attr 'message_count' from device")
        return count
   