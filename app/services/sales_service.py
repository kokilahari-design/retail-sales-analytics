# Service Layer (Business Logic)

from app.models.database import get_connection
from app.utils.logger import get_logger

logger = get_logger(__name__)


#  Database Insertion

def insert_sale_record(data):
    
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = """
        INSERT INTO sales_raw
        (customer_id, customer_name, product_id, product_name, product_category, quantity, price, sale_datetime)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            data["customer_id"], data["customer_name"],data["product_id"], data["product_name"], data["product_category"],
            data["quantity"], data["price"], data["sale_datetime"]
        )

        cursor.execute(query, values)
        connection.commit()
        sale_id = cursor.lastrowid         # cursor.lastrowid gives the auto-incremented primary key of the last row inserted through that cursor.
        connection.close()
        logger.info(f"Inserted sale record {sale_id}")
        return sale_id

    except Exception as e:
        logger.error(f"DB Error: {e}")
        raise
