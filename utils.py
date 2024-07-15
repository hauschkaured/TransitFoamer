from static.interface import *


def static_analyzer(city):
    agency = static_fetcher(city, "agency")
    calendar = static_fetcher(city, "calendar")
    calendar_dates = static_fetcher(city, "calendar_dates")
    routes = static_fetcher(city, "routes")
    shapes = static_fetcher(city, "shapes")
    stop_times = static_fetcher(city, "stop_times")
    stops = static_fetcher(city, "stops")
    trips = static_fetcher(city, "trips")
    print(agency["header"])

# def calendar_feed_checker(calendar):
#     for item in calendar:
#         print(calendar[item])
#         print(type(item))


# def routes_list(routes):
#     for item in routes:
#         print(item)

static_analyzer("pgh")
static_analyzer("sea")
static_analyzer("satx")