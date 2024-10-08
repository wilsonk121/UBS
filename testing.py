import requests
import json

# Define the JSON data to be sent in the POST request
data = \
    [
        {
            "monsters": [1]
        },
        {
            "monsters": [1, 100, 340, 210, 1, 4, 530]
        }
    ]


# Send a POST request to the endpoint /efficient-hunter-kazuma


response = requests.post('https://ubs-yplr.onrender.com/efficient-hunter-kazuma', json=data)# Print the status code
print("Status Code:", response.status_code)

# Print the content (response body)
print("Content:", response.text)
print("Content:", response.headers.get('Content-Type'))