# requests is to send HTTP requests (like GET, POST, PUT, DELETE) and work with APIs easily.

import requests
import logging
from scripts.data_generator import generate_daily_sales_csv
from scripts.data_uploaded_to_hdfs import upload_to_hdfs

logging.basicConfig(level=logging.INFO)

API_URL = "http://127.0.0.1:5000/ingest_sales"

def send_data_to_api(records):
    try:
        response = requests.post(API_URL, json=records, timeout=10)  # sends HTTP POST request to the API endpoint server with the generated sale data as JSON payload
        response.raise_for_status()
        logging.info("Data successfully sent to API")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error("API request failed")
        raise e

def run_pipeline():
    local_file, records = generate_daily_sales_csv()     # Step 1 - Generate Data
    upload_to_hdfs(local_file)                           # Step 2 - Upload to HDFS
    result = send_data_to_api(records)                   # Step 3 - Send Data to SQL staging via API
    return result


if __name__ == "__main__":
    for _ in range(5):
        response = run_pipeline()
        print(response)

   
