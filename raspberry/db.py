import pymongo
import keys
from datetime import datetime

client = pymongo.MongoClient('mongodb://%s:%s@mongo.checinski.dev:27017/wsb-iot-2019' % (keys.username, keys.password))
raspberrydb = client["wsb-iot-2019"]
collection = raspberrydb["pidata"]

raspberrydb["pilogin"].insert_one({"login_time": datetime.now()})
