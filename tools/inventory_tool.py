import pandas as pd

def get_inventory():
    return pd.read_csv("data/inventory_monitoring.csv")

def get_stock_level(product_id):
    inventory = get_inventory()
    result = inventory[inventory['Product ID'] == product_id]
    return result.to_dict(orient='records')
