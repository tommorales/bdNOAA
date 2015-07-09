__author__ = 'tmorales'

import unicodedata
import numpy as np
import matplotlib.pyplot as plt
import cartopy

from pprint import pprint

class ViewMap:

    def plot_geoStation(self, cursor):
        plt.figure(figsize=(15, 15))

        ax = plt.axes(projection=cartopy.crs.PlateCarree())
        ax.set_extent([-15, -180, 90, 0])

        ax.add_feature(cartopy.feature.LAND)
        ax.add_feature(cartopy.feature.OCEAN)
        ax.add_feature(cartopy.feature.COASTLINE)
        ax.add_feature(cartopy.feature.BORDERS, linestyle=':')
        ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
        ax.add_feature(cartopy.feature.RIVERS)
        for doc in cursor:
            print doc
            ax.plot( float(doc["metadata"]["location"]["long"]), float(doc["metadata"]["location"]["lat"]),
                    marker='o', color="r")
        plt.title("Sea Buoy / NOAA")
        #plt.savefig("sea_buoy.png", bbox_inches='tight', pad_inches=0)


class ViewTimeSeries:

    def componente(self, cursor):
        for doc in cursor:
            print doc["products"][0]["t"], doc["products"][0]["v"]