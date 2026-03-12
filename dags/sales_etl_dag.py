# DAG class (Directed Acyclic Graph) creates a new DAG. It defines What tasks exist, In what order they should run, When they should run (schedule), How they behave (retries, timeout, owner, etc.)
# PythonOperator class runs any Python function as airflow task inside a DAG. Airflow tasks must be wrapped inside operators

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
from app.models.database import get_connection
from upload_to_hdfs import uploaded_to_hdfs

#.dt - Datetime accessor to access specialized time-series properties and methods (like .hour, .day, .floor(), etc.)
# .floor('H') - moves the timestamp to the start of the hour. All mins, secs, and microseconds are reset to zero. (Eg., 2025-12-06 14:37:55 becomes 2025-12-06 14:00:00)


def transform_and_load():

    connection = get_connection()
    df = pd.read_sql("SELECT * FROM sales_raw", connection)
    df["Revenue"] = df["quantity"] * df["price"]
    df["hour"] = df["sale_datetime"].dt.floor("h")                     # Grouping sales hour by hour
    summary_df = df.groupby(["hour", "product_name", "product_category"])
                   .agg(total_quantity=("quantity", "sum"),total_revenue=("Revenue", "sum"))
                   .reset_index()                                      # .reset_index() converts groupby result back into a regular DataFrame.

    cursor = connection.cursor()

    for _, row in summary_df.iterrows():

        query = """
        INSERT INTO hourly_sales_summary(aggregation_hour, product_name, product_category, total_quantity, total_revenue)
        VALUES (%s,%s,%s,%s,%s)
        ON DUPLICATE KEY UPDATE                                # ON DUPLICATE KEY UPDATE - If row already exists, MySQL should NOT fail - instead, it should update that existing row.
        total_quantity=VALUES(total_quantity),
        total_revenue=VALUES(total_revenue)
        """

        cursor.execute(query, (
            row["hour"], row["product_name"], row["product_category"],
            row["total_quantity"], row["total_revenue"]
        ))

    connection.commit()
    connection.close()

with DAG(
    dag_id="retail_sales_etl",
    start_date=datetime(2024,1,1),
    schedule_interval='@daily',
    catchup=False
) as dag:
    
    generate_task = PythonOperator(
        task_id="generate_sales_data",
        python_callable=uploaded_to_hdfs
    )

    transform_task = PythonOperator(
        task_id="transform_and_load_task",
        python_callable=transform_and_load
    )
    generate_task >> transform_task
