import json


# Returns needed api Keys 
def getKey(name):
    with open('ApiKeys.json', 'r') as file:
        datafile = file.read()
    keys = json.loads(datafile)
    return str(keys[name])
