# Request Validation Utility : data validation step
    # checks if incoming JSON data from client contains all the necessary key fields.


REQUIRED_FIELDS = [ "customer_id", "customer_name", "product_id", "product_name", "product_category", "quantity", "price", "sale_datetime" ]

def validate_sale_data(data):

    for field in REQUIRED_FIELDS:
        if field not in data:
            return False, f"Missing field {field}"

    return True, "Valid"
