# "Web Requests" Exercise

> Prerequisite:
>   + [Networks, and Processing Data from the Internet](/units/unit-5.md)
>   + [The `requests` Package](/notes/python/packages/requests.md)

## Learning Objectives

  + Practice using Python to request static data files located on the Internet, focusing on "GET" requests.
  + Increase exposure to JSON-formatted data, and practice processing it in Python.
  + Leverage built-in Python modules and third-party Python packages to speed development and enhance capabilities.
  + Prepare to issue requests to get data from web services (APIs).


## Setup






## Challenges


> HINT: the response text for each of the following challenges will be formatted as JSON, so you can use [the `json` module](/notes/python/modules/json.md) to parse it. Also, depending on which URL we are making a request to, sometimes the JSON response will resemble a list and sometimes it will resemble a dictionary, so make sure to parse each accordingly.

### Requesting a Product

Write a Python program which issues a GET request for this [product.json data](https://raw.githubusercontent.com/prof-rossetti/nyu-info-2335-201905/master/data/products/2.json), then prints the product's "name".

> FYI: the response text will be a JSON object, like a Python dictionary

### Requesting Products

Write a Python program which issues a GET request for this [products.json data](https://raw.githubusercontent.com/prof-rossetti/nyu-info-2335-201905/master/data/products.json), then loop through each product and print its "name" and "id" attributes.

> FYI: the response text will be a JSON array of objects, like a Python list of dictionaries

#### Requesting the Gradebook

Write a Python program which issues a GET request for this [gradebook.json data](https://raw.githubusercontent.com/prof-rossetti/nyu-info-2335-201905/master/data/gradebook.json), then calculate and print the average, min, and max grades.
