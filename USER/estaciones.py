__author__ = 'tmorales'

from src.app.controller import Controller

idStation = ["1611400", "1612340", "1615680"]
stateStations = ["HI"]

o = Controller()
o.geo_station(idStations=idStation)
print "*"*40

o.geo_station(stateStations=stateStations)
print "*"*40

o.geo_station(all=True)