# "Shopping Cart" Project

## Further Exploration Challenges

### Challenge 1: Validating User Inputs

When the clerk inputs a product identifier, the program should validate it, displaying a helpful message like "Hey, are you sure that product identifier is correct? Please try again!" if there are no products matching the given identifier.

### Challenge 2: Writing Receipts to File

Create a new directory within the project repository called "receipts".

Instead of, or in addition to, displaying a receipt at the end of the checkout process, the program should write the receipt information into a new `.txt` file saved in the "receipts" directory. The clerk's printer-connected computer should be able to actually print a paper receipt from the information contained in this file.

Each text file should be named according to the date and time the checkout process started (e.g. `/receipts/2017-07-04-15-43-13-579531.txt`, where the numbers represent the year, month, day, 24-hour-style hour, minute, second, and milliseconds/microseconds, respectively).

See [Python file management](/notes/python/file-management.md) for examples of how to write to file.

> NOTE: exclude these receipt files from being tracked in version control by using a ".gitignore" file. If you're not sure, ask the professor.

### Challenge 3: Handling Pricing per Pound

Add a new product called "Organic Bananas" to the products list. Assign it a price of `0.79`, but add another attribute called something like `price_per` to indicate the item is priced per "pound". Update all the other product dictionaries to match the new structure, indicating they are priced per "item".

When running the program, if the clerk inputs the identifier of the bananas (or any other item that is priced by pound), the program should ask the clerk to input the number of pounds (e.g. `2.2`), then the program should calculate the price accordingly.

### Challenge 4: Integrating with Barcode Scanner

Assemble a handful of real products that have barcodes.

Ask to borrow the professor's barcode scanner during class or office hours, or feel free to [purchase one from Amazon](https://www.amazon.com/gp/product/B003OUQ174/ref=ppx_yo_dt_b_asin_title_o03__o00_s00?ie=UTF8&psc=1).

Connect the barcode scanner to your computer's USB port, and practice scanning a few of the items, and record the resulting product identifiers.

Adapt the program's `products` variable to reflect the real products and their identifiers. For example:

```py
# shopping_cart.py
# ...
products = [
    {"id": "99482452704", "name": "Organic Black Beans", "price": 0.99},
    {"id": "99482434182", "name": "Organic Almonds Roasted Unsalted", "price": 7.33},
    {"id": "99482418939", "name": "Jug of Spring Water", "price": 0.99},
    {"id": "898248001107", "name": "Siggi's Strawberry Yogurt", "price": 1.45},
    {"id": "898248001114", "name": "Siggi's Peach Yogurt", "price": 1.45},
    {"id": "290295004269", "name": "Whole Foods Guacamole - Small", "price": 6.50},
    {"id": "012000161155", "name": "LIFE Water", "price": 2.15},
]
# ...
```

> NOTE: for real life products, we'll probably want to change the identifier values to strings, in case any contain alphabetic characters or leading zeros (e.g. "LIFE water" identifier above)

After modifying the product list, try re-running the program, using the barcode scanner to scan the real items. It should work!






<hr>




## Basic Quality Control Challenges

### Formatting Prices

Refactor price-formatting logic into a function called something like `to_usd()`, and implement a corresponding test called something like `test_to_usd()`.

Test various scenarios to ensure the price formatting function displays a dollar sign, two decimal places, and a thousands separator.

### Formatting Timestamps

Refactor timestamp-formatting logic into a function called something like `human_friendly_timestamp()`, and implement a corresponding test called something like `test_human_friendly_timestamp()`.

Test to ensure the function processes any given datetime object into a corresponding human-friendly string.

## Intermediate Quality Control Challenges

### Finding Products

Refactor product-finding logic into a function called something like `find_product()`, and implement a corresponding test called something like `test_find_product()`.

Test various scenarios to ensure the product lookup function finds and returns the proper product, even if the products are not sorted in order of their unique identifiers. What should happen when the function is passed a numeric identifier vs a string identifier? What should happen when there is no product matching the given identifier?

### Calculating Receipt Totals

Refactor subtotal and/or total price calculation logic into one or more function(s) called something like `calculate_total_price()`, and implement a corresponding test(s) called something like `test_calculate_total_price()`.

Test various scenarios to ensure the calculation function(s) produce the proper sum of prices, given a list of selected products and/or product identifiers.
