
# requests is to send HTTP requests (like GET, POST, PUT, DELETE) and work with APIs easily.

import requests
from scripts.upload_to_hdfs import uploaded_to_hdfs

API_URL = "http://127.0.0.1:5000/testing"

for _ in range(5):
    extract_data =  uploaded_to_hdfs()
    response = requests.post(API_URL, json=extract_data)   # sends HTTP POST request to the API endpoint server with the generated sale data as JSON payload
    print(response.json())
   
