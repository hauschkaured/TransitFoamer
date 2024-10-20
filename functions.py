from static.interface import *
from datetime import datetime


import pprint as PP

pp = PP.PrettyPrinter(indent=2)
pprint = pp.pprint


def status_converter(status):
    if status == "IN_TRANSIT_TO": # This is for VIA only
        return "in transit to"
    if status == "STOPPED_AT":
        return "stopped at"


def time_converter(foo):
    time_new = datetime.fromtimestamp(foo).strftime('%H:%M:%S')
    return time_new

def buses_at_stop(data):
    for item in data["bustime-response"]["prd"]:
        if item['prdctdn'] == 'due':
            print(f"{item['rt']} {item['des']} {item['vid']} is DUE.")
            print(f"     Bus is {item['psgld']}")
        else:
            print(f"{item['rt']} {item['des']} {item['vid']} arrives in {item['prdctdn']} minutes.")
            print(f"     Bus is {item['psgld']}")

def bus_trip(foo, trip, vdata, tdata, city):
    bus_data = vdata.entity[foo]
    bus_model = bus_data.vehicle.vehicle.id
    bus_route = bus_data.vehicle.trip.route_id
    routes = static_fetcher(city, "routes")
    stops = static_fetcher(city, "stops")
    trips = static_fetcher(city, "trips")
    route_name = routes[bus_route].route_long_name
    if trip in tdata.entity:
        if trip in trips:
            trip_headsign = trips[trip].trip_headsign
        else:
            trip_headsign = ""
        combined_name = f"\x1b[33mRoute \x1b[34m{bus_route} \x1b[35m{route_name} to \x1b[36m{trip_headsign}\x1b[0m"
        current_trip = tdata.entity[trip]
        current_stop = current_trip.trip_update.stop_time_update[0]
        current_stop_name = stops[current_stop.stop_id].stop_name
        string_return = f"#{bus_model} {combined_name} is in transit to {current_stop_name}"
        if current_stop.arrival is not None and current_stop.departure is not None:
            time_a = time_converter(int(current_stop.arrival.time))
            time_d = time_converter(int(current_stop.departure.time))
            string = f"Arrives at {current_stop_name} at {time_a}. Departs at {time_d}."
        elif current_stop.arrival is not None and current_stop.departure is None:
            time = time_converter(int(current_stop.arrival.time))
            string = f"Arrives at {current_stop_name} at {time}."
        elif current_stop.arrival is None and current_stop.departure is not None:
            time = time_converter(int(current_stop.departure.time))
            string = f"Departs from {current_stop_name} at {time}."
        else:
            string = ''
        print(string_return)
        print(string)
    else:
        combined_name = f"\x1b[33mRoute \x1b[34m{bus_route} \x1b[35m{route_name}\x1b[0m"
        string_return = f"#{bus_model} is not running a route."
        print(string_return)

def buses_in_range(foo, bar, vdata, tdata, city):
    min_int = int(foo)
    max_int = int(bar)
    for i in range(min_int, max_int+1):
        for j in vdata.entity:
            if str(i) == vdata.entity[j].vehicle.vehicle.id:
                bus = vdata.entity[str(i)]
                if bus.vehicle.trip:
                    trip = bus.vehicle.trip.trip_id
                    bus_trip(str(i), trip, vdata, tdata, city)

def buses_on_route(route, vdata, tdata, city):
    route_data = str(route)
    print(f"The following buses are on Route {route_data}:")
    for bus in vdata.entity:
        if vdata.entity[bus].vehicle:
            if vdata.entity[bus].vehicle.trip:
                print(vdata.entity[bus].vehicle.trip.route_id, route_data)
                if vdata.entity[bus].vehicle.trip.route_id == route_data:
                    bus_id = vdata.entity[bus].vehicle.vehicle.id
                    trip = vdata.entity[bus].vehicle.trip.trip_id
                    bus_trip(bus_id, trip, vdata, tdata, city)
