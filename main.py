import requests
import json
from api_key import api_key
import pprint as PP
pp = PP.PrettyPrinter(indent=2)
pprint = pp.pprint


def routeCall():
    URL_base = "https://realtime.portauthority.org/bustime/api/v3/getpredictions?key=yT2htEkvExjjJnKfD22dY6dTT"
    URL_param = "&stpid=10920&format=json"
    print(URL_base + api_key + URL_param)
    predictions = requests.get(f"{URL_base} + {URL_param}")
    bustime = predictions.text
    pprint(bustime)

routeCall()