import datetime
import time
from multiprocessing import Queue
import threading
import pymongo
import numpy

mongo_cluster = pymongo.MongoClient("mongodb+srv://Frujenga:"
                                    "4NkCtRRniz-gdyk@"
                                    "cluster0.2r6kb.mongodb.net/"
                                    "GuardiansDB?retryWrites=true&w=majority")
mongo_database = mongo_cluster["GuardiansDB"]
mongo_collection = mongo_database["GuardiansCollection"]

service_queue = Queue()

SLEEP_INTERVAL = 10


def push_to_database(data_to_push):
    data_to_push["Push_time"] = str.replace(str(datetime.datetime.now()), " ", "T")
    service_queue.put(data_to_push)


def query_last_element():
    return mongo_collection.find_one({}, sort=[('_id', pymongo.DESCENDING)])


def query_all_element():
    return mongo_collection.find_one()


def queue_process():
    print("Queue started!")
    while True:
        time.sleep(SLEEP_INTERVAL)
        print("Queue check!")
        while not service_queue.empty():
            data = service_queue.get()

            hits_avg = numpy.mean(list(data["Hits"].values()))
            data["Hits"]["Average_of_hits"] = hits_avg

            mongo_collection.insert_one(data)


x = threading.Thread(target=queue_process)
x.start()
