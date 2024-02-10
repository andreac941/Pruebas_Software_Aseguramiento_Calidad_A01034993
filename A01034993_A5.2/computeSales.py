# -*- coding: utf-8 -*-
"""ComputeSales.ipynb
This program computes the total cost from a list of items.

"""

import json
import sys
import time

def main():
    """
    Calculate the total sales amount for a given price and quantity.

    Args:
        price (float): The price of a single item.
        quantity (int): The number of items sold.

    Returns:
        float: The total sales amount.
    """
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py TC1.ProductList.json TC1.json")
        sys.exit(1)

    price_catalogue_path = sys.argv[1]
    sales_record_path = sys.argv[2]

    try:
        with open(price_catalogue_path, 'r', encoding="utf-8") as price_catalogue_file:
            price_catalogue_list = json.load(price_catalogue_file)
    except Exception as e:
        print(f"Error reading price catalog file: {e}")
        sys.exit(1)

    try:
        with open(sales_record_path, 'r', encoding="utf-8") as sales_record_file:
            sales_record = json.load(sales_record_file)
    except Exception as e:
        print(f"Error reading sales record file: {e}")
        sys.exit(1)

    price_catalogue = {prod["title"]: prod for prod in price_catalogue_list}

    start_time = time.time()

    total_cost = 0
    for sale in sales_record:
        try:
            product_title = sale['Product']
            quantity = sale['Quantity']
            price = price_catalogue[product_title]['price']
            total_cost += price * quantity
        except KeyError as e:
            print(f"Error processing sale: {e}")

    elapsed_time = time.time() - start_time

    print(f"Total cost: {total_cost}\nElapsed time: {elapsed_time} seconds")

    with open("SalesResults.txt", "w", encoding="utf-8") as r1:
        r1.write(f"Total cost: {total_cost}\nElapsed time: {elapsed_time} seconds")


if __name__ == "__main__":
    main()
