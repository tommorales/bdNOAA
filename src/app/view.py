__author__ = 'tmorales'

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

class ViewMap:

    def plot_geoStation(self, cursor):
        #my_map = self.basemap()
        for doc in cursor:
            print doc["metadata"]["location"]["lat"], doc["metadata"]["location"]["long"]

    def basemap(self):
        """
        Mapa base
        :param cursor: cursor de MongoDB
        :return: objeto my_map
        """
        my_map = Basemap(projection='robin', lat_0=0, lon_0=-100,
              resolution='l', area_thresh=1000.0)
        my_map.drawcoastlines()
        my_map.drawcountries()
        my_map.fillcontinents(color='coral')
        my_map.drawmapboundary()
        my_map.drawmeridians(np.arange(0, 360, 30))
        my_map.drawparallels(np.arange(-90, 90, 30))

        return my_map

