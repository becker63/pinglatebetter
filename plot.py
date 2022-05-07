
from color import colorgen
from calc import PosCitysGen
from geopy.geocoders import Nominatim
import json
import random
import folium
from colormap import rgb2hex
import math
import sys


def gen(ping, player, colorin, mape):
#BEANS
    calc = PosCitysGen(ping)
    places = list(calc.keys())

    file = open("./data/cords.json","r")
    lat_data = json.load(file)

    out = {}
    i = 0
    for key in lat_data:
        cord = lat_data[key]

        for city in places:
            if key == city:
                    print(key + " : " + city)
                    #print(cord)

                    folium.Circle(location=[float(cord[0]), float(cord[1])], popup=f"{player} : {key} : {ping}", fill_color=colorin, radius=200000, weight=2,  color=colorin).add_to(mape)
                    i = i + 1




