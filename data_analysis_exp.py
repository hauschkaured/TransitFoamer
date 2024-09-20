import pandas as pd

# stop_times = pd.read_csv("static/pittsburgh/prt/stop_times.txt")

def route_eq(input):
    if input == 65:
        return True
    else: return False

trips = pd.read_csv("static/pittsburgh/prt/trips.txt")
trips_grouped = trips.groupby("route_id")
trips_grouped.filter(route_eq(["route_id"]))
