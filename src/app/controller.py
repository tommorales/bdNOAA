__author__ = 'tmorales'

import ConfigParser

from .model import Station
from .view import ViewMap

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
        self.__view = ViewMap()

    def geo_station(self, all=False, idStations=None, stateStations=None):
        cursor = self.__modelStation.geo_stations(self.__db, self.__collection, all=all,
                                                 idSations=idStations, stateStation=stateStations)
        self.__view.plot_geoStation(cursor)
