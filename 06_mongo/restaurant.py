# Tim Marder
# SoftDev2 pd06
# K06 -- Yummy Mongo Py
# 2019-03-03

import pymongo
import pprint

SERVER_ADDR = "206.81.3.173"
connection = pymongo.MongoClient(SERVER_ADDR, 27017)
db = connection.test
collection = db.restaurants

def findZip( zip ):
    return collection.find(
                          {"address.zipcode":zip}
                          )

def findBorough( borough ):
    return collection.find(
                          {"borough":borough}
                          )

def findZipGrade( zip , grade ):
    return collection.find(
                          {'$and': [
                                   {"address.zipcode":zip},
                                   {"grades.0.grade":grade}
                                   ]
                          })

def findZipScore( zip , score ):
    return collection.find(
                          {'$and': [
                                   {"address.zipcode":zip},
                                   {"grades.0.grade":score}
                                   ]
                          })
