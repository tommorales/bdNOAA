__author__ = 'tmorales'

import ConfigParser

from .model import Station
from .model import Data
from .view import ViewMap
from .view import ViewTimeSeries

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
        self.__collection2 = "ocean_data"

        self.__modelStation = Station(self.__host, self.__port)
        self.__modelData = Data(self.__host, self.__port)
        self.__view = ViewMap()
        self.__viewTimeSerie = ViewTimeSeries()

    def geo_station(self, all=False, idStations=None, stateStations=None):
        cursor = self.__modelStation.geo_stations(self.__db, self.__collection, all=all,
                                                 idSations=idStations, stateStation=stateStations)
        self.__view.plot_geoStation(cursor)

    def timeSerie(self, componente):
        cursor = self.__modelData.timeSerie_componente(self.__db, self.__collection2,
                                                       componente)
        self.__viewTimeSerie.componente(cursor)

    def valores(self, stations):
        cursor = self.__modelData.valor_componentes_stations(self.__db, self.__collection2,
                                                             stations)
        for doc in cursor:
            print doc
