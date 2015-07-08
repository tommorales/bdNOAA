__author__ = 'tmorales'

from pprint import pprint

from src.templateMongoDB import QueryTemplate
from ..conector import Conector

class Station:
    def __init__(self, host, port):
        self.__conection= Conector(host, port)

    def geo_staions(self, db, collection, all=False, staions=None):
        collecStation= self.__conection.mongodb(db, collection)
        print collecStation
        if all is True:
            pass
        if staions is not None:
            pass
        pprint(collecStation.find_one())





