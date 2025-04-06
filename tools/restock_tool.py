import json

def restock_tool(product_id, suggested_qty):
    return {
        "status": "Request Sent",
        "product_id": product_id,
        "quantity": suggested_qty
    }
