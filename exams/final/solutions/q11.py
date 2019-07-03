
salads = [
    {"id": 1, "name": "Caesar", "price": 8.99},
    {"id": 2, "name": "Chicken Caesar", "price": 11.99},
    {"id": 3, "name": "Waldorf", "price": 10.99},
    {"id": 4, "name": "Cobb", "price": 9.99},
    {"id": 5, "name": "Caprese", "price": 9.99},
    {"id": 6, "name": "Nicoise", "price": 10.99},
]

#
# QUESTION 11-A
#
# Assuming the identifier, or ​"id"​ attribute, of each salad is and will always be unique,
# ... and assuming the order of salads may vary,
# ... "print" the name of the salad whose identifier is equal to ​3​ (i.e. ​"Waldorf"​):
#

# SOLUTION

matching_salads = [salad for salad in salads if salad["id"] == 3]
matching_salad = matching_salads[0]
print(matching_salad["name"])

# ALTERNATIVE SOLUTION

matching_salads = []

for salad in salads:
    if salad["id"] == 3:
        matching_salads.append(salad)

matching_salad = matching_salads[0]
print(matching_salad["name"])

# ALTERNATIVE SOLUTION

for salad in salads:
    if salad["id"] == 3:
        print(salad["name"])

#
# QUESTION 11-B
#
# Assuming the ​"price"​ attribute represents a salad’s cost to the consumer,
# ... "print" the number of salads which are more expensive than ten dollars (i.e. ​3​):
#

# SOLUTION

expensive_salads = [salad for salad in salads if salad["price"] > 10]

print(len(expensive_salads))

# ALTERNATIVE SOLUTION

expensive_salads = []

for salad in salads:
    if salad["price"] > 10:
        expensive_salads.append(salad)

print(len(expensive_salads))
