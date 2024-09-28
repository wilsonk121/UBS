import requests
import json

# Define the JSON data to be sent in the POST request
data = \
    [
        {
             "bugseq": [[20,30],[30,400],[110,1350],[200,3330]]
        },
        {
             "bugseq": [[3,2],[4,3]]
        }
    ]


# Send a POST request to the endpoint /efficient-hunter-kazuma


#response = requests.post('http://127.0.0.1:5000/bugfixer/p2', json=data)# Print the status code
response = requests.post('https://ubs-yplr.onrender.com/bugfixer/p2', json=data)# Print the status code
print("Status Code:", response.status_code)
print("Content:", response.text)
print("Content:", response.headers.get('Content-Type'))