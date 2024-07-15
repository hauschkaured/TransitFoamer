import json

with open('data/realtime_feeds.json') as f:
    d = json.load(f)
    print(d)