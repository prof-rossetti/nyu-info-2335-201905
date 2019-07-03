from rideshare import trip

#
# QUESTION 10-F
#
# Define a custom function called ​promotional_message​
# ... which accepts an input parameter called ​driver​
# ... and "returns" (NOT "prints") a textual message about that given driver.
#
# ... Valid ​driver​ parameter values are assumed to resemble the structure of the one found within the provided ​trip​ variable
# ... (i.e. has attributes indicating the driver’s first name, last name, average rating, and number of total trips).
#
# ... In the event the given driver’s average rating is greater than ​4.5,
# ... then the message should include language about the driver’s average rating
# ... (e.g. "Your driver has an average rating of 4.8"​, where 4.8 refers to the given driver’s average rating).
# ... Otherwise, the message should include language about the number of trips the given driver has completed
# ... (e.g.​ "Your driver has completed 100 trips",​ where 100 refers to the given driver’s total trips).
#
# ... The function’s invocation has been written for you below.
# ... Write the function’s definition below such that it will be able to be invoked in the manner prescribed.
#

# FUNCTION DEFINITION

def promotional_message(driver):
    if driver["avg_rating"] > 4.5:
        message = "DRIVER HAS GOOD RATING: " + str(driver["avg_rating"])
    else:
        message = "DRIVER HAS LOTS OF TRIPS: " + str(driver["total_rides"])
    return message

# FUNCTION INVOCATIONS

print(promotional_message(trip["driver"]))

my_driver = trip["driver"]
print(promotional_message(my_driver))

other_driver = {
    "first_name": "Otto",
    "last_name": "Other",
    "avg_rating": 4.9,
    "total_rides": 30
}
print(promotional_message(other_driver))
