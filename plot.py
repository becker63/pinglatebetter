
from color import colorgen
from calc import PosCitysGen
from geopy.geocoders import Nominatim
import json
import random
import folium
from colormap import rgb2hex
import math
import sys

mape = folium.Map(location = [25, 0], zoom_start=3)
folium.TileLayer('cartodbdark_matter').add_to(mape)

def debugnamegen():
    f = open('/tmp/wordlist.txt', 'r')
    p = f.read().split("\n")
    return random.choice(p)


def gen(ping, player, colorin):
#BEANS
    calc = PosCitysGen(ping)
    places = list(calc.keys())

    file = open("cords.json","r")
    lat_data = json.load(file)

    out = {}
    i = 0
    for key in lat_data:
        cord = lat_data[key]

        for city in places:
            if key == city:
                    print(key + " : " + city)
                    #print(cord)

                    folium.Circle(location=[float(cord[0]), float(cord[1])], popup=f"{player} : {key}", fill_color=colorin, radius=200000, weight=2,  color=colorin).add_to(mape)
                    i = i + 1


a = colorgen(10)

for item in a:
    gen(random.randint(1, 100), debugnamegen(), item)

mape.save('index.html') 