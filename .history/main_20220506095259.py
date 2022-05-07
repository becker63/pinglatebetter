import json
from plot import gen
from color import colorgen
import folium 
import random 
from flask import Flask
from flask import render_template
from flask_restful import Resource, Api
from flask import Flask, request, jsonify

app = Flask(__name__)

def autohtmlrealoadinsert():
    with open("./templates/index.html",'r+') as f:
        lines=f.readlines()
        column=4
        line=3
        word='<meta http-equiv="refresh" content="5">'

        lines[line]=lines[line][0:column]+word+lines[line][column:]
        f.seek(0)

        for i in lines:        
            f.write(i)



playercolors = colorgen(300)
playercolorum = 0


mape = folium.Map(location = [25, 0], zoom_start=3)

oldplayer = ""

data = {}

def main():
    global data
    global playercolorum
    global mape
    folium.TileLayer('cartodbdark_matter').add_to(mape)

    
    for i in data:
    
        ping = int(data[i])
        player = i

       if ping < len(playercolors):
           gen(ping, player, playercolors[ping], mape)
       else:
           gen(ping, player, playercolors[len(playercolors) - 1], mape)
       playercolorum = playercolorum + 1
   
       autohtmlrealoadinsert()




@app.route('/', methods=['PUT'])
def create_record():
    global data
    data = json.loads(request.data)

    main()

    mape.save('./templates/index.html') 
    return ("ok!")

@app.route("/")
def hello():
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
