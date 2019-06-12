import json

import requests

def get_products():
    request_url = "https://groceries-api-csv.herokuapp.com/products"
    response = requests.get(request_url)
    #print(response.status_code)
    return json.loads(response.text)

def get_product(product_id):
    request_url = f"https://groceries-api-csv.herokuapp.com/products/{product_id}"
    response = requests.get(request_url)
    #print(response.status_code)
    return json.loads(response.text)

#
# DRAFT CODE NEEDS TESTING AND REVISION...
#
#def create_product(product_attrs):
#    print("CREATING A NEW PRODUCT...")
#    request_url = "https://groceries-api-csv.herokuapp.com/products"
#    response = requests.post(request_url, json=product_attrs)
#    print(response.status_code)
#    return json.loads(response.text)
#
#def update_product(product_id, product_attrs):
#    print(f"UPDATING PRODUCT #{product_id}...")
#    request_url = f"https://groceries-api-csv.herokuapp.com/products/{product_id}"
#    response = requests.put(request_url, json=product_attrs)
#    print(response.status_code)
#
#def delete_product(product_id):
#    print(f"DELETING PRODUCT #{product_id}...")
#    request_url = f"https://groceries-api-csv.herokuapp.com/products/{product_id}"
#    response = requests.delete(request_url)
#    print(response.status_code)

if __name__ == "__main__":

    print("------------")
    print("GETTING ALL PRODUCTS...")

    products = get_products()

    for p in products:
        print(f"{p['id']} ... {p['name']} ... {p['price']}")

    product_id = products[0]["id"] # input("Please select a product identifier")

    print("------------")
    print(f"GETTING PRODUCT '{product_id}'...")

    product = get_product(product_id)
    print(product)
