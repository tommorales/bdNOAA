__author__ = 'tmorales'

import datetime as dt
from pprint import pprint

from src.templateMongoDB import QueryTemplate
from ..conector import Conector

class Station:
    def __init__(self, host, port):
        self.__conection= Conector(host, port)

    def geo_stations(self, db, collection, all=False, idSations=None, stateStation=None):
        collecStation= self.__conection.mongodb(db, collection)

        if all is True:
            query = {}
        if idSations is not None:
            query = {"-ID": {"$in": idSations}}
        if stateStation is not None:
            query = {"metadata.location.state": {"$in": stateStation}}
        projection = {"_id":0, "-name":1, "metadata.location":1}

        return collecStation.find(query, projection)


class Data:
    def __init__(self, host, port):
        self.__conection = Conector(host, port)

    def timeSerie_componente(self, db, collection, componente):

        collecStation= self.__conection.mongodb(db, collection)

        query = {"$and":[
            {"products.t": {"$gte": dt.datetime(2014, 8, 8, 0, 0),
                            "$lte": dt.datetime(2014, 8, 18, 0, 0)}},
            {'station_id': 9461380}
            ]}
        projection = {
            "_id": 0, "name": 1,
            "products": {"$elemMatch": {"name": componente}}
                      }

        return collecStation.find(query, projection)

    def average(self, db, collection, byName=False, byYearByProducts=False,
                byYearByProducto=False, byYearMontDay=False):
        if byName is True:
            # get averages grouped by name
            pass

        if byYearByProducts is True:
            # get average values group by year, and by product
            pass

        if byYearByProducto is True:
            # get average values group by year, and by product, where product = selected
            pass

        if byYearMontDay is True:
            #get average values, group by year/month/day for water temp in August 2014
            pass





