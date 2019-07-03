from rideshare import trip

#
# QUESTION 10-E
#
# "Print" the total fare for this trip.
# ... The total fare is equal to the sum of all individual stop fares (i.e. ​$17.98)​.
# ... It is not necessary to round or adjust decimal places, but do include a dollar sign.
#

# SOLUTION:

fares = [stop["fare"] for stop in trip["stops"]]

total_fare = sum(fares)

print("$" + str(total_fare)) # or using interpolation would be fine here as well, like:
print(f"${total_fare}")

# ALTERNATIVE SOLUTION:

total_fare = 0

for stop in trip["stops"]:
    total_fare = total_fare + stop["fare"]

print("$" + str(total_fare)) # or using interpolation would be fine here as well, like:
print(f"${total_fare}")
