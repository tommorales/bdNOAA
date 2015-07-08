__author__ = 'tmorales'

import ConfigParser

from .modelAnalitica import Station

class Controller:

    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read("..config.cfg")

        #self.__host= config.get("mongodb", "hostname")
        #self.__port = config.getint("mongodb", "puerto")
        #self.__db =  config.get("mongodb", "db")
        #self.__collection = config.get("mongodb", "coleccion_metadatos")
        self.__host = "localhost"
        self.__port = 27017
        self.__db = "noaa"
        self.__collection = "stations"

        self.__modelStation = Station(self.__host, self.__port)

    def geo_station(self, all=False, stations=None):
        self.__modelStation.geo_staions(self.__db, self.__collection)