import json

strength = 1

def math(ping, test):
    p1 = ping - strength
    p2 = ping + strength

    for i in range(p1, p2):
        #print(i)

        if i == test:
            return True


def PosCitysGen(playerping):
    file = open("./data/lat_data.json","r")
    lat_data = json.load(file)

    out = {}
    for key in lat_data:
        value = lat_data[key]

        if math(playerping, int(value)) == True:
            #print(f"{key} = {value}")
            out.update({key:float(value)})
    return out


