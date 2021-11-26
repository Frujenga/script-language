import datetime
import time
from multiprocessing import Queue, Process
import pymongo
import numpy


mongo_cluster = pymongo.MongoClient("mongodb+srv://Frujenga:"
                                      "4NkCtRRniz-gdyk@"
                                      "cluster0.2r6kb.mongodb.net/"
                                      "GuardiansDB?retryWrites=true&w=majority")
mongo_database = mongo_cluster["GuardiansDB"]
mongo_collection = mongo_database["GuardiansCollection"]




