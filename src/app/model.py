__author__ = 'tmorales'

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




