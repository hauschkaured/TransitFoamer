trips = open("pittsburgh/trips.txt", "r").read()
for line in trips:
    for item in line.split(","):


