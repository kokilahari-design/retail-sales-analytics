# Simulates sales event

import random
from datetime import datetime

CUSTOMER_NAMES = ["kokila", "Sandy", "Kalai", "Hari", "Viswa", "Sharvesh", "Vedanth", "Hema", "Deebika", "David", "Henry"]
CUSTOMER_MAP = {i+1: name for i, name in enumerate(CUSTOMER_NAMES)}

products = [
    ("Laptop", "Electronics", 1000.00),
    ("Phone", "Electronics", 800.00),
    ("Shoes", "Fashion", 499.00)
]

def generate_sale_event():

    product = random.choice(products)

    return {
        "customer_id": random.choice(list(CUSTOMER_MAP.keys())) 
        "customer_name": CUSTOMER_MAP[customerid]
        "product_id": random.randint(100,200),
        "product_name": product[0],
        "product_category": product[1],
        "quantity": random.randint(1,5),
        "price": product[2],
        "sale_datetime": datetime.now().isoformat()
    }
