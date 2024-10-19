from static.interface import static_fetcher
import json
import pprint as PP

pp = PP.PrettyPrinter(indent=2)
pprint = pp.pprint

def merge_dicts(dict1, dict2):
    pprint(dict2)

def static_analyzer(city):
    # agency = static_fetcher(city, "agency")
    # calendar = static_fetcher(city, "calendar")
    # calendar_dates = static_fetcher(city, "calendar_dates")
    routes = static_fetcher(city, "routes")
    # shapes = static_fetcher(city, "shapes")
    stop_times = static_fetcher(city, "stop_times")
    # stops = static_fetcher(city, "stops")
    trips = static_fetcher(city, "trips")

    route_list = routes_list(routes)
    trips_per_route_dict = trips_per_route(trips, route_list)
    stops_per_trip(trips, stop_times)


def routes_list(routes):
    data_list = []
    for route in routes:
        data = routes[route]
        data_list.append(data.route_id)
    return data_list


def trips_per_route(trips, route_list):
    trips_per_route_dict = dict()
    for route in route_list:
        list_of_trips = []
        for trip in trips:
            if trips[trip].route_id == route:
                list_of_trips.append(trips[trip].trip_id)
        trips_per_route_dict[route] = list_of_trips
    return trips_per_route_dict
    

def stops_per_trip(trips, stop_times):
    trip_stop_dict = dict()
    for trip in trips:
        print(trip)
        stop_list = []
        for stop_line in stop_times:
            print(trips[trip].trip_id)
            print(stop_times[stop_line].trip_id)
            if trips[trip].trip_id == stop_times[stop_line].trip_id:
                stop_list.append(stop_times[stop_line].stop_id)
        trip_stop_dict[trip] = stop_list
    string = json.dumps(trip_stop_dict)
    write_to_file("static/stops_per_trip", string)
        


def stops_per_route(trips_per_route_dict, stop_times, trips):
    stops_dict = dict()
    for route in trips_per_route_dict:
        stop_list = []
        for trip in trips_per_route_dict[route]:
            for stop_line in stop_times:
                if stop_times[stop_line].trip_id == trip:
                    stop_list.append(stop_times[stop_line].stop_id)
        stops_dict[route] = stop_list
    pprint(stops_dict)


def write_to_file(path: str, content: str) -> None:
    """
    Writes the content string to the specified path
    """
    with open(path, 'w') as f:
        f.write(content)       
    

static_analyzer("pgh")
