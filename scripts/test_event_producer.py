
# requests is to send HTTP requests (like GET, POST, PUT, DELETE) and work with APIs easily.

import requests
from scripts.data_generator import generate_sale_event

API_URL = "http://127.0.0.1:5000/testing"

for _ in range(5):
    data = generate_sale_event()
    response = requests.post(API_URL, json=data)   # sends HTTP POST request to the API endpoint server with the generated sale data as JSON payload
    print(response.json())
  
