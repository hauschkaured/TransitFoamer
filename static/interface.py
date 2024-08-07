import pprint as PP

pp = PP.PrettyPrinter(indent=2)
pprint = pp.pprint


class Agency:
    def __init__(self, agency_id, agency_name, agency_url, agency_timezone, agency_lang, agency_phone, agency_fare_url,
                 agency_email):
        self.agency_id = agency_id
        self.agency_name = agency_name
        self.agency_url = agency_url
        self.agency_timezone = agency_timezone
        self.agency_lang = agency_lang
        self.agency_phone = agency_phone
        self.agency_fare_url = agency_fare_url
        self.agency_email = agency_email

    def __repr__(self):
        return f'''{self.agency_id},{self.agency_name},{self.agency_url},{self.agency_timezone},{self.agency_lang}, 
        {self.agency_phone},{self.agency_fare_url},{self.agency_email}'''


class Calendar:
    def __init__(self, service_id, monday, tuesday, wednesday, thursday, friday,
                 saturday, sunday, start_date, end_date):
        self.service_id = service_id
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.sunday = sunday
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f"""{self.service_id} {self.monday} {self.tuesday} {self.wednesday} {self.thursday} {self.friday}
        {self.friday} {self.saturday} {self.sunday} {self.start_date} {self.end_date}"""


class CalendarDates:
    def __init__(self, service_id, date, exception_type):
        self.service_id = service_id
        self.date = date
        self.exception_type = exception_type

    def __repr__(self):
        return f"{self.service_id} {self.date} {self.exception_type}"


class Feed:
    def __init__(self, feed_publisher_name, feed_publisher_url, feed_lang, default_lang, feed_start_date, feed_end_date,
                 feed_version, feed_contact_email, feed_contact_url):
        self.feed_publisher_name = feed_publisher_name
        self.feed_publisher_url = feed_publisher_url
        self.feed_lang = feed_lang
        self.default_lang = default_lang
        self.feed_start_date = feed_start_date
        self.feed_end_date = feed_end_date
        self.feed_version = feed_version
        self.feed_contact_email = feed_contact_email
        self.feed_contact_url = feed_contact_url

    def __repr__(self):
        return f'''{self.feed_publisher_name} {self.feed_publisher_url} {self.feed_lang} {self.default_lang} 
        {self.feed_start_date} {self.feed_end_date} {self.feed_version} {self.feed_contact_email} {self.feed_contact_url}'''


class Levels:
    def __init__(self, level_id, level_index, level_name):
        self.level_id = level_id
        self.level_index = level_index
        self.level_name = level_name

    def __repr__(self):
        return f'''{self.level_id} {self.level_index} {self.level_name}'''


class Routes:
    def __init__(self, route_id, agency_id, route_short_name, route_long_name, route_desc, route_type, route_url,
                 route_color, route_text_color, route_sort_color, continuous_pickup, continuous_drop_off, network_id):
        self.route_id = route_id
        self.agency_id = agency_id
        self.route_short_name = route_short_name
        self.route_long_name = route_long_name
        self.route_desc = route_desc
        self.route_type = route_type
        self.route_url = route_url
        self.route_color = route_color
        self.route_text_color = route_text_color
        self.route_sort_color = route_sort_color
        self.continuous_pickup = continuous_pickup
        self.continuous_drop_off = continuous_drop_off
        self.network_id = network_id

    def __repr__(self):
        return f'''{self.route_id} {self.agency_id} {self.route_short_name} {self.route_long_name}
        {self.route_desc} {self.route_type} {self.route_url} {self.route_color} {self.route_text_color}
        {self.route_sort_color} {self.continuous_pickup} {self.continuous_drop_off} {self.network_id}'''


class Shapes:
    def __init__(self, shape_id, shape_pt_lat, shape_pt_lon, shape_pt_sequence, shape_dist_traveled):
        self.shape_id = shape_id
        self.shape_pt_lat = shape_pt_lat
        self.shape_pt_lon = shape_pt_lon
        self.shape_pt_sequence = shape_pt_sequence
        self.shape_dist_traveled = shape_dist_traveled

    def __repr__(self):
        return f'''{self.shape_id} {self.shape_pt_lat} {self.shape_pt_lon} 
        {self.shape_pt_sequence} {self.shape_dist_traveled}'''


class StopTimes:
    def __init__(self, trip_id, arrival_time, departure_time, stop_id, location_group_id, location_id, stop_sequence,
                 stop_headsign, start_pickup_drop_off_window, end_pickup_drop_off_window, pickup_type, drop_off_type,
                 continuous_pickup, continuous_drop_off, shape_dist_traveled, timepoint, pickup_booking_rule_id,
                 drop_off_booking_rule_id):
        self.trip_id = trip_id
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        self.stop_id = stop_id
        self.location_group_id = location_group_id
        self.location_id = location_id
        self.stop_sequence = stop_sequence
        self.stop_headsign = stop_headsign
        self.start_pickup_drop_off_window = start_pickup_drop_off_window
        self.end_pickup_drop_off_window = end_pickup_drop_off_window
        self.pickup_type = pickup_type
        self.drop_off_type = drop_off_type
        self.continuous_pickup = continuous_pickup
        self.continuous_drop_off = continuous_drop_off
        self.shape_dist_traveled = shape_dist_traveled
        self.timepoint = timepoint
        self.pickup_booking_rule_id = pickup_booking_rule_id
        self.drop_off_booking_rule_id = drop_off_booking_rule_id

    def __repr__(self):
        return f'''{self.trip_id}: {self.arrival_time} {self.departure_time} {self.stop_id} {self.location_group_id} 
        {self.location_id} {self.stop_sequence} {self.stop_headsign} {self.start_pickup_drop_off_window} 
        {self.end_pickup_drop_off_window} {self.pickup_type} {self.drop_off_type} {self.continuous_pickup} 
        {self.continuous_drop_off} {self.shape_dist_traveled} {self.timepoint} {self.pickup_booking_rule_id} 
        {self.drop_off_booking_rule_id}'''


class Stops:
    def __init__(self, stop_id, stop_code, stop_name, tts_stop_name, stop_desc, stop_lat, stop_lon, zone_id,
                 stop_url, location_type, parent_station, stop_timezone, wheelchair_boarding, level_id, platform_code):
        self.stop_id = stop_id
        self.stop_code = stop_code
        self.stop_name = stop_name
        self.tts_stop_name = tts_stop_name
        self.stop_desc = stop_desc
        self.stop_lat = stop_lat
        self.stop_lon = stop_lon
        self.zone_id = zone_id
        self.stop_url = stop_url
        self.location_type = location_type
        self.parent_station = parent_station
        self.stop_timezone = stop_timezone
        self.wheelchair_boarding = wheelchair_boarding
        self.level_id = level_id
        self.platform_code = platform_code

    def __repr__(self):
        return f"""{self.stop_id}: {self.stop_code} {self.stop_name} {self.tts_stop_name} {self.stop_desc}
        {self.stop_lat} {self.stop_lon} {self.zone_id} {self.stop_url} {self.location_type} {self.parent_station} 
        {self.stop_timezone} {self.wheelchair_boarding}"""


class Transfers:
    def __init__(self, from_stop_id, to_stop_id, from_route_id, to_route_id, from_trip_id, to_trip_id,
                 transfer_type, min_transfer_time):
        self.from_stop_id = from_stop_id
        self.to_stop_id = to_stop_id
        self.from_route_id = from_route_id
        self.to_route_id = to_route_id
        self.from_trip_id = from_trip_id
        self.to_trip_id = to_trip_id
        self.transfer_type = transfer_type
        self.min_transfer_time = min_transfer_time

    def __repr__(self):
        return f'''{self.from_stop_id} {self.to_stop_id} {self.from_route_id} {self.to_route_id}
        {self.from_trip_id} {self.to_trip_id} {self.transfer_type} {self.min_transfer_time}'''


class Trips:
    def __init__(self, route_id, service_id, trip_id, trip_headsign, trip_short_name,
                 direction_id, block_id, shape_id, wheelchair_accessible, bikes_allowed):
        self.route_id = route_id
        self.service_id = service_id
        self.trip_id = trip_id
        self.trip_headsign = trip_headsign
        self.trip_short_name = trip_short_name
        self.direction_id = direction_id
        self.block_id = block_id
        self.shape_id = shape_id
        self.wheelchair_accessible = wheelchair_accessible
        self.bikes_allowed = bikes_allowed

    def __repr__(self):
        return f'''{self.route_id} {self.service_id} {self.trip_id} {self.trip_headsign} 
        {self.trip_short_name} {self.direction_id} {self.block_id} {self.shape_id} 
        {self.wheelchair_accessible} {self.bikes_allowed}'''


def text_processing(text, function, foo):
    # Dictionaries to return
    agency = dict()
    calendar_dates = dict()
    calendar = dict()
    routes = dict()
    shapes = dict()
    stop_times = dict()
    stops = dict()
    trips = dict()
    # Reading the data 
    data = text.read().splitlines()
    # header = data[0]
    # #  Header debug
    # if function == "agency":
    #     agency["header"] = header
    # elif function == "calendar":
    #     calendar["header"] = header
    # elif function == "calendar_dates":
    #     calendar_dates["header"] = header
    # elif function == "routes":
    #     routes["header"] = header
    # elif function == "shapes":
    #     shapes["header"] = header
    # elif function == "stops":
    #     stops["header"] = header
    # elif function == "stop_times":
    #     stop_times["header"] = header
    # elif function == "trips":
    #     trips["header"] = header
    removed_header = data[1:]
    for line in removed_header:
        items = line.split(',')
        if function == "agency": # Configured normally
            if (foo == "manhattan" or foo == "nyc_subway" or foo == "brooklyn" or foo == "queens" or foo == "bronx"
            or foo == "staten_island"):
                agency_id = items[0]
                agency_name = items[1]
                agency_url = items[2]
                agency_timezone = items[3]
                agency_lang = items[4]
                agency_phone = items[5]
                obj = Agency(agency_id, agency_name, agency_url, agency_timezone, agency_lang,
                             agency_phone, None, None)
            elif foo == "chicago":
                agency_name = items[0]
                agency_url = items[1]
                agency_timezone = items[2]
                agency_lang = items[3]
                agency_phone = items[4]
                agency_fare_url = items[5]
                obj = Agency(None, agency_name, agency_url, agency_timezone, agency_lang,
                             agency_phone, agency_fare_url, None)
            else:
                agency_id = items[0]
                agency_name = items[1]
                agency_url = items[2]
                agency_timezone = items[3]
                agency_lang = items[4]
                agency_phone = items[5]
                agency_fare_url = items[6]
                obj = Agency(agency_id, agency_name, agency_url, agency_timezone, agency_lang,
                             agency_phone, agency_fare_url, None)
            agency[foo] = obj
        elif function == "calendar_dates":
            service_id = items[0]
            date = items[1]
            exception_type = items[2]
            obj = CalendarDates(service_id, date, exception_type)
            calendar_dates[(service_id, date)] = obj
        elif function == "calendar":
            service_id = items[0]
            monday = items[1]
            tuesday = items[2]
            wednesday = items[3]
            thursday = items[4]
            friday = items[5]
            saturday = items[6]
            sunday = items[7]
            start_date = items[8]
            end_date = items[9]
            obj = Calendar(service_id, monday, tuesday, wednesday, thursday, friday, saturday,
                        sunday, start_date, end_date)
            calendar[service_id] = obj
        elif function == "routes":
            if foo == "manhattan" or foo == "brooklyn" or foo == "queens" or foo == "bronx" or foo == "staten_island":
                route_id = items[0]
                agency_id = items[1]
                route_short_name = items[2]
                route_long_name = items[3]
                route_desc = items[4]
                route_type = items[5]
                route_color = items[6]
                route_text_color = items[7]
                obj = Routes(route_id, agency_id, route_short_name, route_long_name,
                            route_desc, route_type, None, route_color,
                            route_text_color, None, None, None, None)
            elif foo == "nyc_subway":
                agency_id = items[0]
                route_id = items[1]
                route_short_name = items[2]
                route_long_name = items[3]
                route_type = items[4]
                route_desc = items[5]
                route_url = items[6]
                route_color = items[7]
                route_text_color = items[8]
                obj = Routes(route_id, agency_id, route_short_name, route_long_name,
                             route_desc, route_type, route_url, route_color,
                             route_text_color, None, None, None, None)
            elif foo == "chicago":
                route_id = items[0]
                route_short_name = items[1]
                route_long_name = items[2]
                route_type = items[3]
                route_url = items[4]
                route_color = items[5]
                route_text_color = items[6]
                obj = Routes(route_id, None, route_short_name, route_long_name,
                             None, route_type, route_url, route_color, route_text_color,
                             None, None, None, None)
            else:
                route_id = items[0]
                agency_id = items[1]
                route_short_name = items[2]
                route_long_name = items[3]
                route_desc = items[4]
                route_type = items[5]
                route_url = items[6]
                route_color = items[7]
                route_text_color = items[8]
                obj = Routes(route_id, agency_id, route_short_name, route_long_name,
                             route_desc, route_type, route_url, route_color, route_text_color,
                             None, None, None, None)
            routes[route_id] = obj
        elif function == "shapes": # Configured Normally
            if foo == "nyc_subway":
                shape_id = items[0]
                shape_pt_sequence = items[1]
                shape_pt_lat = items[2]
                shape_pt_lon = items[3]
                obj = Shapes(shape_id, shape_pt_lat, shape_pt_lon, shape_pt_sequence, None)
            elif foo == "manhattan" or foo == "brooklyn" or foo == "queens" or foo == "bronx" or foo == "staten_island":
                shape_id = items[0]
                shape_pt_lat = items[1]
                shape_pt_lon = items[2]
                shape_pt_sequence = items[3]
                obj = Shapes(shape_id, shape_pt_lat, shape_pt_lon, shape_pt_sequence, None)
            else:
                shape_id = items[0]
                shape_pt_sequence = items[1]
                shape_pt_lat = items[2]
                shape_pt_lon = items[3]
                shape_dist_traveled = items[4]
                obj = Shapes(shape_id, shape_pt_lat, shape_pt_lon, shape_pt_sequence, shape_dist_traveled)
            shapes[id] = obj
        elif function == "stop_times":
            if foo == "manhattan" or foo == "brooklyn" or foo == "queens" or foo == "bronx" or foo == "staten_island":
                trip_id = items[0]
                arrival_time = items[1]
                departure_time = items[2]
                stop_id = items[3]
                stop_sequence = items[4]
                pickup_type = items[5]
                drop_off_type = items[6]
                timepoint = items[7]
                obj = StopTimes(trip_id, arrival_time, departure_time, stop_id, None, None,
                                stop_sequence, None, None, None,
                                pickup_type, drop_off_type, None, None, None, timepoint,
                                None, None)
            elif foo == "nyc_subway":
                trip_id = items[0]
                stop_id = items[1]
                arrival_time = items[2]
                departure_time = items[3]
                stop_sequence = items[4]
                obj = StopTimes(trip_id, arrival_time, departure_time, stop_id, None, None,
                                stop_sequence, None, None, None,
                                None, None, None, None, None, None,
                                None, None)
            elif foo == "chicago":
                trip_id = items[0]
                arrival_time = items[1]
                departure_time = items[2]
                stop_id = items[3]
                stop_sequence = items[4]
                stop_headsign = items[5]
                pickup_type = items[6]
                shape_dist_traveled = items[7]
                obj = StopTimes(trip_id, arrival_time, departure_time, stop_id, None, None,
                                stop_sequence, stop_headsign, None, None,
                                pickup_type, None, None, None, shape_dist_traveled, None,
                                None, None)
            else:
                trip_id = items[0]
                arrival_time = items[1]
                departure_time = items[2]
                stop_id = items[3]
                stop_sequence = items[4]
                stop_headsign = items[5]
                pickup_type = items[6]
                drop_off_type = items[7]
                shape_dist_traveled = items[8]
                timepoint = items[9]
                obj = StopTimes(trip_id, arrival_time, departure_time, stop_id, None, None,
                                stop_sequence, stop_headsign, None, None,
                                pickup_type, drop_off_type, None, None, shape_dist_traveled, timepoint,
                                None, None)
            stop_times[(trip_id, stop_sequence)] = obj
        elif function == "stops": # Configured normally
            if foo == "nyc_subway":
                stop_id = items[0]
                stop_name = items[1]
                stop_lat = items[2]
                stop_lon = items[3]
                location_type = items[4]
                parent_station = items[5]
                obj = Stops(stop_id, None, stop_name, None, None, stop_lat, stop_lon,
                            None, None, location_type, parent_station, None, None, None, None)

            elif foo == "manhattan" or foo == "brooklyn" or foo == "queens" or foo == "bronx" or foo == "staten_island":
                stop_id = items[0]
                stop_name = items[1]
                stop_desc = items[2]
                stop_lat = items[3]
                stop_lon = items[4]
                zone_id = items[5]
                stop_url = items[6]
                location_type = items[7]
                parent_station = items[8]
                obj = Stops(stop_id, None, stop_name, None, stop_desc, stop_lat, stop_lon, zone_id,
                            stop_url, location_type, parent_station, None, None, None, None)
            elif foo == "chicago":
                stop_id = items[0]
                stop_code = items[1]
                stop_name = items[2]
                stop_desc = items[3]
                stop_lat = items[4]
                stop_lon = items[5]
                location_type = items[6]
                parent_station = items[7]
                wheelchair_boarding = items[8]
                obj = Stops(stop_id, stop_code, stop_name, None, stop_desc, stop_lat, stop_lon, None,
                            None, location_type, parent_station, None, None, None, None)
            else:
                stop_id = items[0]
                stop_code = items[1]
                stop_name = items[2]
                stop_desc = items[3]
                stop_lat = items[4]
                stop_lon = items[5]
                zone_id = items[6]
                stop_url = items[7]
                location_type = items[8]
                parent_station = items[9]
                stop_timezone = items[10]
                wheelchair_boarding = items[11]
                obj = Stops(stop_id, stop_code, stop_name, None, stop_desc, stop_lat, stop_lon, zone_id,
                            stop_url, location_type, parent_station, stop_timezone, wheelchair_boarding, None, None)
            stops[stop_id] = obj
        elif function == "trips":
            if foo == "nyc_subway":
                route_id = items[0]
                trip_id = items[1]
                service_id = items[2]
                trip_headsign = items[3]
                direction_id = items[4]
                shape_id = items[5]
                obj = Trips(route_id, service_id, trip_id, trip_headsign, None,
                            direction_id, None, shape_id, None, None)
            elif foo == "manhattan" or foo == "brooklyn" or foo == "queens" or foo == "bronx" or foo == "staten_island":
                route_id = items[0]
                service_id = items[1]
                trip_id = items[2]
                trip_headsign = items[3]
                direction_id = items[4]
                block_id = items[5]
                shape_id = items[6]
                obj = Trips(route_id, service_id, trip_id, trip_headsign, None,
                            direction_id, block_id, shape_id, None, None)
            elif foo == "chicago":
                route_id = items[0]
                service_id = items[1]
                trip_id = items[2]
                direction_id = items[3]
                block_id = items[4]
                shape_id = items[5]
                wheelchair_accessible = items[6]
                # schd_trip_id = items[7]  # EXCLUSIVE TO THE CTA, NOT IN THE STANDARD FEED!
                obj = Trips(route_id, service_id, trip_id, None, None,
                            direction_id, block_id, shape_id, wheelchair_accessible, None)
            elif foo == "pgh":
                trip_id = items[0]
                route_id = items[1]
                service_id = items[2]
                trip_headsign = items[3]
                trip_short_name = items[4]
                direction_id = items[5]
                block_id = items[6]
                shape_id = items[7]
                wheelchair_accessible = items[8]
                bikes_allowed = items[9]
                obj = Trips(route_id, service_id, trip_id, trip_headsign, trip_short_name,
                            direction_id, block_id, shape_id, wheelchair_accessible, bikes_allowed)
            elif foo == "seattle":
                route_id = items[0]
                service_id = items[1]
                trip_id = items[2]
                trip_headsign = items[3]
                trip_short_name = items[4]
                direction_id = items[5]
                block_id = items[6]
                shape_id = items[7]
                # peak_flag = items[8]  # SEATTLE EXCLUSIVE
                # fare_id = items[9]  # SEATTLE EXCLUSIVE
                wheelchair_accessible = items[10]
                bikes_allowed = items[11]
                obj = Trips(route_id, service_id, trip_id, trip_headsign, trip_short_name,
                            direction_id, block_id, shape_id, wheelchair_accessible, bikes_allowed)
            else:
                route_id = items[0]
                service_id = items[1]
                trip_id = items[2]
                trip_headsign = items[3]
                trip_short_name = items[4]
                direction_id = items[5]
                block_id = items[6]
                shape_id = items[7]
                wheelchair_accessible = items[8]
                bikes_allowed = items[9]
                obj = Trips(route_id, service_id, trip_id, trip_headsign, trip_short_name,
                            direction_id, block_id, shape_id, wheelchair_accessible, bikes_allowed)
            trips[trip_id] = obj
    if function == "agency":
        return agency
    elif function == "calendar_dates":
        return calendar_dates
    elif function == "calendar":
        return calendar
    elif function == "routes":
        return routes
    elif function == "shapes":
        return shapes
    elif function == "stop_times":
        return stop_times
    elif function == "stops":
        return stops
    elif function == "trips":
        return trips


def static_fetcher(foo, function):
    if foo == "pgh":
        url = "static/pittsburgh/prt/" + f"{function}" + ".txt"
    elif foo == "satx":
        url = "static/san_antonio/via/" + f"{function}" + ".txt"
    elif foo == "seattle":
        url = "static/seattle/king_county/" + f"{function}" + ".txt"
    elif foo == "manhattan":
        url = "static/new_york/mta_bus_manhattan/" + f"{function}" + ".txt"
    elif foo == "nyc_subway":
        url = "static/new_york/mta_subway/" + f"{function}" + ".txt"
    elif foo == "brooklyn":
        url = "static/new_york/mta_bus_brooklyn/" + f"{function}" + ".txt"
    elif foo == "queens":
        url = "static/new_york/mta_bus_queens/" + f"{function}" + ".txt"
    elif foo == "chicago":
        url = "static/chicago/cta/" + f"{function}" + ".txt"
    elif foo == "bronx":
        url = "static/new_york/mta_bus_bronx/" + f"{function}" + ".txt"
    elif foo == "staten_island":
        url = "static/new_york/mta_bus_staten_island/" + f"{function}" + ".txt"
    else:
        url = ""
    text = open(url, "r")
    result = text_processing(text, function, foo)
    return result
