import http.client as http
http._MAXHEADERS = 1000
from os.path import exists
import requests
import json
import re

def pingscrape(GameHostCity):
    #clear the file
    file = open("lat_data.json","w")
    file.truncate(0)
    file.close()

    GameHostCityurl = ('https://wondernetwork.com/pings/' + GameHostCity.replace(" ", "%20"))
    mystr = requests.get(url = GameHostCityurl).text
    out = mystr.split("\n")

    returned = {}
    for line in out:
        if 'href="/pings/New York/' in line:
            placere = re.search('k/(.*)"', line)
            place = placere.group(1)
            msre = re.search('>(.*)ms', line)
            ms = msre.group(1)

            returned.update({place:float(ms)})

    with open('lat_data.json', 'w') as outfile:
        json.dump(returned, outfile, indent = 4)


pingscrape('New York')