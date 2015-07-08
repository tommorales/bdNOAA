__author__ = 'tmorales'

import ConfigParser

config = ConfigParser.ConfigParser()
config.read("config.cfg")

hostname= config.get("mongodb", "hostname")
port= config.getint("mongodb", "puerto")
db= config.get("mongodb", "db")
stations= config.get("mongodb", "coleccion_metadatos")
ocean_data= config.get("mongodb", "coleccion_datos")


print hostname