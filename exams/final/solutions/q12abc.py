from rideshare import trip

#
# QUESTION 10-A
#
# “Print” a human-friendly message to denote the driver’s first name (i.e. ​“Your driver is Danny”)​:
#

# SOLUTION:

print("Your driver is " + trip["driver"]["first_name"])

# ALTERNATIVE SOLUTION:

print(f"Your driver is {trip['driver']['first_name']}")

# ALTERNATIVE SOLUTION:

print("Your driver is", trip["driver"]["first_name"])

#
# QUESTION 10-B
#
# “Print” the number of stops this trip makes (i.e.​ 3)​:
#

# SOLUTION:

print(len(trip["stops"]))

# ALTERNATIVE SOLUTION:

n = 0

for stop in trip["stops"]:
    n = n + 1

print(n)

#
# QUESTION 10-C
#
# Assuming the stops will always be listed in ascending order of their stop sequence,
# ... “print” the name of the passenger who is traveling to the first stop (i.e. ​“Vishal”)​:
#

# SOLUTION:

print(trip["stops"][0]["passenger"])

# ALTERNATIVE SOLUTION (ACCEPTED BUT NOT INTENDED):

for stop in trip["stops"]:
    if stop["sequence"] == 1:
        print(stop["passenger"])
