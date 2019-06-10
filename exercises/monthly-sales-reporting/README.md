# The "Sales Reporting" Exercise

> Prerequisites:
>   + [Datastores, and Processing CSV Data](/units/unit-4.md)
>   + The [`csv`](/notes/python/modules/csv.md) and [`itertools`](/notes/python/modules/itertools.md) Modules, or [The `pandas` Package](/notes/python/packages/pandas.md)

## Learning Objectives

  + Create a new Python application to automate a business process.
  + Practice using Python to process CSV files.
  + Practice researching and leveraging the capabilities provided by Python modules and third-party packages.

## Business Prompt

Assume you own and operate a successful small business, selling artisan clothing products through an online platform like Amazon, Etsy, or eBay.

![hoodie for sale on etsy](https://user-images.githubusercontent.com/1328807/51781151-cb7a5300-20e2-11e9-863f-3b82aaa5f5a9.png)

At the end of each calendar month, the online platform makes available for download from its admin interface a CSV file representing all individual sales orders for that month. See the ["monthly sales data"](/data/monthly-sales) examples (row per day per product sold that day).

To aid your ability to make data-driven decisions, you decide to create a Python program which will automate the process of gleaning business insights from the monthly sales data.

## Setup

Create a new exercise repository called "sales-reporting" somewhere on your computer, perhaps on your Desktop.

Download any one of the ["monthly sales data"](/data/monthly-sales) CSV files into your exercise repository, either in the root directory or inside a new sub-directory called "data".

Create a new Python script called something like "sales_reporter.py" and place inside some temporary Python code like `print("SALES REPORT (MONTH YEAR)")` inside. Then save the file and make your first commit with a message like "Setup exercise repo".

## Instructions

Adapt the contents of the "sales_reporter.py" script to process the CSV file to display a human-readable representation of the given month and year and the total sales for that month.

Example output:

```
SALES REPORT (MARCH 2018)

TOTAL SALES: $12,000.71
```

## Further Exploration

Optionally adapt your script to also identify the three top-selling products for that month and the total sales for each.

Example output:

```
SALES REPORT (MARCH 2018)

TOTAL SALES: $12,000.71

TOP SELLING PRODUCTS:
  1. Button-Down Shirt: $6,960.35
  2. Super Soft Hoodie: $1,875.00
  3. etc.
```
