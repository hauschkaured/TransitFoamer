# TransitFoamer

For doing stuff with transit GTFS-RT data.
Disclaimer: This project is not currently in a well-developed state. 

# Dependencies

This project was written in Python 3.12. It makes use of the `requests` module to 
fetch data from URLs. It makes use of the `protobuf` package to parse the protobuf
binary encodings that are fetched from the URLs.

# Use

To use TransitFoamer, simply run the file `main_new.py` with `python3`.

# Outline

`main_new.py` runs the interactive layer of the program.
`fetcher.py` grabs the GTFS-RT data from the URL to which it is provided, outputs a dictionary.
`trip_processing.py` converts the output dictionary from `fetcher`

# Version List

v0.5
Significant reworking to base functions done. PRT API calls still not totally integrated into app. 
Two key files added: 
- realtime_interface.py
- static/interface.py
These provide descriptions of the data hierarchically and classify the data into a manner which corresponds
to the GTFS specification. 

v0.4.2
Added PRT API for more detailed information about vehicles and added the ability to 
track bus stop predicted arrivals. 

v0.4.1 
Refactoring project so main functionalities are centralized and run independent of
the selected organization.

v0.4
Reworking the app to stay away from API use and migrate to agency-provided GTFS-RT 
feeds. Current cities planned to have support: Pittsburgh, San Antonio. Converted 
all GTFS static feed files to python files with associated classes and methods. 
Currently have basic functions such as "find route" working. 

v0.3.2 (April 25, 2024)
- Changed name of project from transit-api to TransitFoamer.

v0.3.1 (Mar 29, 2024)
- Added option to foam entire series of buses to app, have not implemented it yet. 

v0.3 (Mar 28, 2024)
- Now have a rudimentary foaming mode done. Supports up to 10 buses as CSV with no
space between entries. TODO: Clean up the displayed messages.

v0.2: (Mar 27, 2024)
- Now have route tracking done (loosely). Enter route followed by list of route(s)
to obtain all buses on a given route. 

v0.1: (Mar 26, 2024)
- Currently have bus stop tracking done. If user enters bus followed by bus stop
numbers, then result is a list of buses which arrive at bus stop. If multiple bus
stops are entered, then result includes list of buses with the stop at which they
arrive.
- Moved files to Pittsburgh directory.
- Changed file name from predictions.py to transit.py.

v0.1: (Mar 26, 2024)
- Currently have bus stop tracking done. If user enters bus followed by bus stop
numbers, then result is a list of buses which arrive at bus stop. If multiple bus
stops are entered, then result includes list of buses with the stop at which they
arrive.
- Moved files to Pittsburgh directory.
- Changed file name from predictions.py to transit.py.