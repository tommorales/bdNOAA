__author__ = 'tmorales'

import pymongo


class Conector:
    def __init__(self, host, port):
        self.__host= host
        self.__port= port

    def mongodb(self, db, collection):

        try:
            client = pymongo.MongoClient(self.__host, self.__port)
            db = client[db]
            collection = db[collection]
        except pymongo.errors.ConnectionFailure, e:
            print "Could not connect to server: %s" % e
        return collection

