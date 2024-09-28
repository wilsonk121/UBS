import requests
import json

# Define the JSON data to be sent in the POST request
data = \
[
    {
      "dictionary": ["purjle", "rocket", "silver", "gadget", "window", "dragon"],
      "mistypes": ["purqle", "gadgat", "socket", "salver"],
    }
]

# Send a POST request to the endpoint /efficient-hunter-kazuma


#response = requests.post('http://127.0.0.1:5000/the-clumsy-programmer', json=data)# Print the status code
response = requests.post('https://ubs-yplr.onrender.com/the-clumsy-programmer', json=data)# Print the status code
print("Status Code:", response.status_code)
print("Content:", response.json())
print("Content:", response.headers.get('Content-Type'))