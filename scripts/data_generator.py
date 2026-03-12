# Simulates sales event
import random
import pandas as pd
from datetime import datetime

CUSTOMER_NAMES = ["kokila", "Sandy", "Kalai", "Hari", "Viswa", "Sharvesh", "Vedanth", "Hema", "Deebika", "David", "Henry"]

CUSTOMER_MAP = {i+1: name for i, name in enumerate(CUSTOMER_NAMES)}

products = [
    ("Laptop", "Electronics", 1000.00),
    ("Phone", "Electronics", 800.00),
    ("Shoes", "Fashion", 499.00)
]


def generate_sale_event():

    customer_id = random.choice(list(CUSTOMER_MAP.keys()))
    product = random.choice(products)

    return {
        "customer_id": customer_id,
        "customer_name": CUSTOMER_MAP[customer_id],
        "product_id": random.randint(100, 200),
        "product_name": product[0],
        "product_category": product[1],
        "price": product[2],
        "quantity": random.randint(1, 5),
        "sale_datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def generate_daily_sales_csv():

    records = []
    for _ in range(100):   # generate 100 records
        records.append(generate_sale_event())

    df = pd.DataFrame(records)
    filename = f"/tmp/sales_{datetime.now().date()}.csv"

    df.to_csv(filename, index=False)
    print("CSV generated:", filename)

    return filename


if __name__ == "__main__":
    generate_daily_sales_csv()
