# shopping_cart.py

#from pprint import pprint

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# print(products)
# pprint(products)

# TODO: write some Python code here to produce the desired output


#
# INFO CAPTURE / INPUT
# User puts in a number, the code reads the data and provides and output

# loop function

total_price = 0
selected_ids = []

while True:
    selected_id = input("Please input a product identifier: ") #> "9" (string data type)
    #> "DONE"
    if selected_id == "DONE":
        break
    else:
        #print(selected_id) #prints the number that was input
        #print(type(selected_id)) #tells us the data type/format
        # matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
        # matching_product = matching_products[0] #
        # total_price = total_price + matching_product["price"]
        #print("SELECTED PRODUCT: " + matching_product["name"] + " " + str(matching_product["price"])) #Don't want to print select product immediately after each time
        selected_ids.append(selected_id)
#print(selected_ids)
#print(matching_product)
#print(type(matching_product)) #tells us what the matching_product type is (list data type - note that str and list are different)

#
# INFO DISPLAY / OUTPUT
#

print("---------------------------------")
print("BRYAN'S WHOLEFOODS GROCERY")
print("WWW.BRYANS-WHOLEFOODS-GROCERY.COM")
print("---------------------------------")

from datetime import datetime
# now = datetime.now()
# time = now.strftime("%H:%M:%S")

now = datetime.now()
date_time = now.strftime("%m/%d/%Y, %I:%M %p")

print("CHECKOUT AT:" + " " + str(date_time)) #> '2017-07-02'

print("---------------------------------")

for selected_id in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0] #
    total_price = total_price + matching_product["price"]
    print("... " + matching_product["name"] + " " + str(matching_product["price"]))

print("---------------------------------")

#print("SUBTOTAL: " + str(total_price)) #TODO format in USD

print("SUBTOTAL: ${0:.2f}".format(total_price)) #TODO format in USD

tax_rate = .0875 #NY tax rate 8.75%
tax = float(total_price) * tax_rate

print("TAX: ${0:.2f}".format(tax))

print("TOTAL: ${0:.2f}".format(total_price + tax))

print("---------------------------------")
print("THANK YOU FOR SHOPPING AT BRYAN'S WHOLEFOODS")
print("---------------------------------")

# my_price = str(total_price)

# def to_usd(my_price):
#     """
#     Converts a numeric value to usd-formatted string, for printing and display purposes. \n
#     Example: to_usd(4000.444444) \n
#     Returns: $4,000.44
#     """
#     return f"${my_price:,.2f}"


# A grocery store name of your choice
# A grocery store phone number and/or website URL and/or address of choice
# The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2019-06-06 11:31 AM)
# The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $1.50)
# The total cost of all shopping cart items, formatted as US dollars and cents (e.g. $4.50), calculated as the sum of their prices
# The amount of tax owed (e.g. $0.39), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax)
# The total amount owed, formatted as US dollars and cents (e.g. $4.89), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items
