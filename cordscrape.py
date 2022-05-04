import http.client as http
from geopy.geocoders import Nominatim
http._MAXHEADERS = 1000
from os.path import exists
import requests
import json
import re


def addrtocord(address):
    geolocator = Nominatim(user_agent="GetLoc")
    location = geolocator.geocode(address)
    return((location.latitude, location.longitude))

def cordscrape():
    #clear the file
    file = open("cords.json","w")
    file.truncate(0)
    file.close()

    mystr = requests.get(url = 'https://wondernetwork.com/pings/New%20York').text
    out = mystr.split("\n")

    returned = {}
    i = 0
    for line in out:
        if 'href="/pings/New York/' in line:
            placere = re.search('k/(.*)"', line)
            place = placere.group(1)
            a = addrtocord(place)

            returned.update({place:a})

            b = list(returned.items())
            print(f"{i}    " + str(b[i]))
            i = i + 1

            with open('cords.json', 'w') as outfile:
                json.dump(returned, outfile, indent = 4)



