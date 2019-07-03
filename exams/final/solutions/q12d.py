from rideshare import trip

#
# QUESTION 10-D
#
# Loop through each of the trip’s stops and "print" that stop’s destination, one at a time
# ... (i.e. "Madison Square", then "Union Square", then "Washington Square", each on its own line):
#

# SOLUTION:

for stop in trip["stops"]:
    print(stop["destination"])

# ALTERNATIVE SOLUTION (ACCEPTED BUT NOT INTENDED):

destinations = [stop["destination"] for stop in trip["stops"]]
for d in destinations:
    print(d)

# ALTERNATIVE SOLUTION (ACCEPTED BUT NOT INTENDED):

[print(stop["destination"]) for stop in trip["stops"]]

# ALTERNATIVE SOLUTION (ACCEPTED BUT NOT INTENDED):

stop_count = len(trip["stops"])

for i in range(0, stop_count):
    print(trip["stops"][i]["destination"])

# ALTERNATIVE SOLUTION (ACCEPTED BUT NOT INTENDED):

i = 0
stop_count = len(trip["stops"])

while i < stop_count:
    print(trip["stops"][i]["destination"])
    i = i + 1
