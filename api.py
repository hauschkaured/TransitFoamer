import requests
import pprint as PP

pp = PP.PrettyPrinter(indent=2)
pprint = pp.pprint
def call(x):
    with open("data/apikey.txt", "r") as base:
        key = base.read()

    API_URL = "https://truetime.portauthority.org/bustime/api/v3/"
    BASE_PARAMS = {
        'key': key, 
        'format': 'json',
        'rtpidatafeed': 'Port Authority Bus',
        'stpid': {x}
    }

    print("1: Making HTTPS request.")
    data1 = requests.get(API_URL + "getpredictions", params=BASE_PARAMS)

    if data1: 
        print("2: Success!")
    else:
        raise Exception(f"2: Non-success status code: {data1.status_code}")

    print("3: Unpacking Content")

    data2 = data1.json()
    return data2
