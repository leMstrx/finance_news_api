"""
This file is for testing the API 
"""

import requests

url = 'http://127.0.0.1:5000/news/all'
headers = {'API-Key': 'y4PrzvW42lchwrNf1XeKcQ'}

response = requests.get(url, headers=headers)

print("Test")
print(response.json())