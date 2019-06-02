# Python Datatypes (a.k.a. "Groceries") Exercise

> Prerequisites:
>   + [Software Products and Services](/units/unit-1.md)
>   + [User Interfaces and Experiences (UI/UX)](/units/unit-2.md)
>   + [Python Language Overview](/units/unit-3.md)

## Learning Objectives

  + Gain familiarity with the Python programming language and its building-blocks, or "datatypes".
  + Learn how to write your first Python script from scratch!
  + Practice processing an information input into a desired information output.

## Setup

Create a new directory on your Desktop called "python-datatypes", then navigate there from the command-line.

Within that directory, create a new file called `groceries.py` and place inside the following code:

```python
# groceries.py

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

print(products)

# TODO: write some Python code here to produce the desired output
```

Create and activate a new Anaconda virtual environment (e.g. "groceries-env"), or feel free to use the "base" environment because we don't need to install any packages to complete this exercise.

Within the virtual environment, run the Python script and watch it print the list of products:

```sh
python groceries.py
```

Great, setup is complete and you are now ready to start development.

## Instructions

Inside the Python script, write Python code which will transform the data into the following output:

    --------------
    THERE ARE 20 PRODUCTS:
    --------------
     + All-Seasons Salt ($4.99)
     + Chocolate Fudge Layer Cake ($18.50)
     + Chocolate Sandwich Cookies ($3.50)
     + Cut Russet Potatoes Steam N' Mash ($4.25)
     + Dry Nose Oil ($21.99)
     + Fresh Scent Dishwasher Cleaner ($4.99)
     + Gluten Free Quinoa Three Cheese & Mushroom Blend ($3.99)
     + Green Chile Anytime Sauce ($7.99)
     + Light Strawberry Blueberry Yogurt ($6.50)
     + Mint Chocolate Flavored Syrup ($4.50)
     + Overnight Diapers Size 6 ($25.50)
     + Peach Mango Juice ($1.99)
     + Pizza For One Suprema Frozen Pizza ($12.50)
     + Pomegranate Cranberry & Aloe Vera Enrich Drink ($4.25)
     + Pure Coconut Water With Orange ($3.50)
     + Rendered Duck Fat ($9.99)
     + Robust Golden Unsweetened Oolong Tea ($2.49)
     + Saline Nasal Mist ($16.00)
     + Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce ($6.99)
     + Sparkling Orange Juice & Prickly Pear Beverage ($2.99)
    --------------
    THERE ARE 10 DEPARTMENTS:
    --------------
     + Babies (1 product)
     + Beverages (5 products)
     + Dairy Eggs (1 product)
     + Dry Goods Pasta (1 product)
     + Frozen (4 products)
     + Household (1 product)
     + Meat Seafood (1 product)
     + Pantry (2 products)
     + Personal Care (2 products)
     + Snacks (2 products)

## Checkpoints

The "checkpoint" steps below provide one example strategy for breaking-up the larger problem into smaller, more manageable pieces. Feel free but not obligated to follow these checkpoints, working through one step at a time before moving on to the next.

### Checkpoint 1 - Printing Products

  1. Print all products (already done for you! :smiley_cat:).
  2. Print the number of products.
  3. Print the first product.
  4. Print the name of the first product.
  5. Print the name of each product.
  6. Print in alphabetical order the name of each product.
  7. Print in alphabetical order the name and price of each product.
  8. Print in alphabetical order the name and price of each product, where the price is rounded to two decimal places.

### Checkpoint 2 - Printing Departments

  1. Print the number of unique departments.
  2. Print the name of each unique department.
  3. Print in alphabetical order the name of each unique department.
  4. Print in alphabetical order the name of each unique department, as well as the number of products associated with that department.
  5. Print in alphabetical order the name of each unique department, as well as the number of products associated with that department, and properly differentiate between "products" plural and "product" singular, depending on how many there are.

## Submission Instructions

In a subsequent class, the professor will guide you through the process uploading your code to GitHub.
