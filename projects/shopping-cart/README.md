# "Shopping Cart" Project

![a screencast of a user running a python script from a terminal](https://user-images.githubusercontent.com/1328807/50870741-53442b80-1387-11e9-9180-ab96688c6590.gif)

## Business Prompt

Your local corner grocery store has hired you as a technology consultant to help modernize their checkout system.

Currently, the store affixes a price tag sticker on each grocery item in stock and uses a calculator at the checkout counter to add up the product prices and calculate tax and total amount due.

Instead, the store owner describes a desired checkout process which involves a checkout clerk scanning each product's barcode to automatically look up product prices, perform tax and total calculations, and print a customer receipt.

## Learning Objectives

  1. Create a tool to facilitate and streamline a business process.
  2. Gain familiarity with processing and validating user inputs in Python.
  3. Reinforce introductory Python programming concepts such as datatypes, functions, variables, and loops.

## Requirements

Write a program that asks the user to input one or more product identifiers, then looks up the prices for each, then prints an itemized customer receipt including the total amount owed.

The program should use a provided list of dictionaries (see setup instructions below) to represent the store owner's database of products and prices.

The program should prompt the checkout clerk to input the identifier of each shopping cart item, one at a time. At any time the clerk should be able to indicate there are no more shopping cart items by inputting the word `DONE`.

After the clerk indicates there are no more items, the program should print a custom receipt on the screen. The receipt should include the following components:

  + A grocery store name of your choice.
  + A grocery store phone number and/or website URL and/or address of choice.
  + The date and time of the beginning of the checkout process, formatted in a human-friendly way.
  + The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. `$1.50`).
  + The total cost of all shopping cart items, formatted as US dollars and cents (e.g. `$4.50`), calculated as the sum of their prices.
  + The amount of tax owed, calculated by multiplying the total cost by a District of Columbia sales tax rate of 6%.
  + The total amount owed, formatted as US dollars and cents (e.g. `$4.77`), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items.
  + A friendly message thanking the customer and/or encouraging the customer to shop again.

The program should be able to process multiple shopping cart items of the same kind, but need not display any groupings or aggregations of those items (although it may optionally do so).

### Example Output

``` sh
(shopping-env)  --->> python shopping_cart.py
Please input a product identifier: 1
Please input a product identifier: 8
Please input a product identifier: 6
Please input a product identifier: 8
Please input a product identifier: 8
Please input a product identifier: 16
Please input a product identifier: 12
Please input a product identifier: DONE
#> ---------------------------------
#> GREEN FOODS GROCERY
#> WWW.GREEN-FOODS-GROCERY.COM
#> ---------------------------------
#> CHECKOUT AT: 2019-02-02 11:31 AM
#> ---------------------------------
#> SELECTED PRODUCTS:
#>  ... Chocolate Sandwich Cookies ($3.50)
#>  ... Cut Russet Potatoes Steam N' Mash ($4.25)
#>  ... Dry Nose Oil ($21.99)
#>  ... Cut Russet Potatoes Steam N' Mash ($4.25)
#>  ... Cut Russet Potatoes Steam N' Mash ($4.25)
#>  ... Mint Chocolate Flavored Syrup ($4.50)
#>  ... Chocolate Fudge Layer Cake ($18.50)
#> ---------------------------------
#> SUBTOTAL: $61.24
#> TAX: $3.67
#> TOTAL: $64.91
#> ---------------------------------
#> THANKS, SEE YOU AGAIN SOON!
#> ---------------------------------
```

## Setup

### From Starter

To setup your project repository, either fork and clone the professor's ["Shopping Cart" Starter Repository](https://github.com/prof-rossetti/shopping-cart-starter-py), or follow the steps below to setup your own from scratch.

### From Scratch

Take this time to create a new repository on GitHub.com called something like "shopping-cart-project". We'll refer to this as your "remote project repository".

Clone or download the remote project repository onto your local machine, perhaps on your Desktop. We'll refer to this as your "local project repository".

Navigate to your local project repository from the command-line.

Within the local project repository, create a new file called `shopping_cart.py` and place inside the following contents:

```python
# shopping_cart.py

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

# TODO: write some Python code here to produce the desired functionality...
print(products)
```

Create a new virtual environment named something like "shopping-cart-env" and activate it. Then from inside the virtual environment, execute the Python script to see it print the list of products.

Finally, make your first commit with a message like "Setup project repository", and push these changes to GitHub. Once you see these changes reflected in your remote project repository on GitHub.com, you are ready to start the project development process.




## Development

As you develop your project repository, incrementally "commit" your work along the way. By the time you are finished with development, your project repository should contain a version history including at least a handful of incremental commits.

### Checkpoints

If you're not sure where to start, feel free to adopt the development approach recommended in the ["Shopping Cart" Checkpoints](shopping-cart/checkpoints.md).

### Further Exploration

If you're able to complete the basic project requirements with relative ease, consider addressing one or more of the ["Shopping Cart" Further Exploration Challenges](shopping-cart/further.md) (e.g. writing receipts to file, integrating with a real-life barcode scanner, etc.).

## Submission

To submit your project:

  1. Push your local project repository to GitHub, so you can visit your remote project repository at a URL like `https://github.com/YOUR_USERNAME/shopping-cart-project`.
  2. Fork the ["upstream" course repository](https://github.com/prof-rossetti/georgetown-opim-243-201901) (or refresh your existing fork).
  3. Update your forked course repository's ["Shopping Cart" Submissions CSV file](shopping-cart/submissions.csv).
to include your GitHub username and your project repository's URL.
  4. Submit a Pull Request for your forked course repository's changes to be accepted into the "upstream" course repository.

## Evaluation

Project submissions will be evaluated according to the requirements set forth above, as summarized by the rubric below:

Category | Requirement | Weight
--- | --- | ---
Info Inputs | Captures / scans product identifiers | 10%
Info Inputs | Handles the "DONE" signal | 10%
Info Outputs (Receipt) | Displays store info | 10%
Info Outputs (Receipt) | Displays checkout date and time | 10%
Info Outputs (Receipt) | Displays names and prices of all scanned products | 20%
Info Outputs (Receipt) | Displays tax and totals | 20%
Dev Process | Submitted via Git repository which reflects an incremental revision history | 20%

If experiencing execution error(s) while evaluating the application's required functionality, evaluators are advised to reduce the project's grade by anywhere between 15% and 50%, depending on the circumstances and severity of the error(s).

In recognition of deliverables which exhibit functionality above and beyond the basic required functionality, evaluators are encouraged to award between 0.5% and 3.0% extra credit "engagement points" to be applied towards the final exam.
