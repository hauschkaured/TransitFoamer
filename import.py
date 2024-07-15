import json
import pprint as PP
from fetcher import main
pp = PP.PrettyPrinter(indent=2)
pprint = pp.pprint

with open('data/realtime_feeds.json') as f:
    dict = json.load(f)
    pprint(dict)


test = dict["seattle"]
pprint(test)
for key in test:
    url = test[key]


