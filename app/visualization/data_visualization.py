import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from app.models.database import get_connection

def generate_revenue_chart():
    connection = get_connection()
    query = """
    SELECT aggregation_hour, total_revenue FROM hourly_sales_summary
    ORDER BY aggregation_hour
    """

    df = pd.read_sql(query, connection)
    connection.close()

    plt.figure()
    plt.plot(df["aggregation_hour"], df["total_revenue"])
    plt.title("Revenue Trend")
    buffer = BytesIO()                      # Save to in-memory buffer instead of disk file
    plt.savefig(buffer, format="png") 
    buffer.seek(0)                          # Reset buffer pointers and return the buffers

    return buffer
