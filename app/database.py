# pymysql - load the MySQL connector library so Python program can talk to your MySQL database.

import pymysql

# Database Connection Configuration

DB_CONFIG = {
    'host': "localhost",
    "user" : "root",                                                     # type for user name
    "password" : "kokila",                                               # type your password
    "database" : "retail_analytics"
}


#route() function of the Flask class is a decorator. route() decorator is used to bind URL(API endpoind) to a function(record_sale).
# GET - Retrieve or check data (optional in your API), POST - Send/submit data (your sale event) to server. Here POST method used to create a new resource
@app.route('/testing', methods = ['POST']) 
def record_sale():
    connection = None  # Initialize connection to None
    cursor = None      # Initialize cursor to None
    # .get_json() method reads the JSON sent by the client and turns it into a Python dictionary.
    data = request.get_json()
    print(f"Received data: {data}")

    # 1. data validation step: checks if incoming JSON data from client contains all the necessary key fields.
    # Built-in function "all" returns True only if all keys exist in data. The "not" operator inverts the result.
    # jsonify({"msg": "error msg returned to client"}), 400 (Status code - Bad Request due to invalid or missing data)
    # cursor.lastrowid gives the auto-incremented primary key of the last row inserted through that cursor.
    if not all(k in data for k in ("customer_id", "customer_name", "product_id", "product_name", "product_category", "quantity", "price", "sale_datetime")):
        return jsonify({"message": "Missing required fields"}), 400
    
    # 2. Database Insertion
    try:
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()
        insert_query = """
        INSERT INTO sales_raw (customer_id, customer_name, product_id, product_name, product_category, quantity, price, sale_datetime)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (data["customer_id"], data["customer_name"], data["product_id"],data["product_name"],data["product_category"],data["quantity"],data["price"], data["sale_datetime"])
        cursor.execute(insert_query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Sale recorded successfully", "order_id": cursor.lastrowid}), 201
    except Exception as e:
        print(f"Error during DB Connection: {e}")
        return jsonify({"message": "Database error", "error": str(e)}), 500
    finally:
        print("Execution completed.")
