import requests
import json

# Define the JSON data to be sent in the POST request
data = \
    [{'bugseq': [[20, 30], [110, 135], [30, 150], [210, 330]]}, {'bugseq': [[3, 2], [4, 3]]}, {'bugseq': [[5, 7]]},
     {'bugseq': [[1, 3], [2, 5], [3, 10]]}, {'bugseq': [[100, 90], [200, 180], [300, 270]]},
     {'bugseq': [[1, 10], [2, 10], [3, 10]]}, {'bugseq': [[5, 15], [10, 20], [15, 25], [20, 30]]},
     {'bugseq': [[10, 20], [10, 25]]},
     {'bugseq': [[1, 100], [2, 200], [3, 300], [4, 400], [5, 500], [6, 600], [7, 700], [8, 800], [9, 900], [10, 1000]]},
     {'bugseq': [[2, 5], [2, 6], [2, 7]]}, {'bugseq': [[2, 5], [3, 6], [5, 8]]}]

# Send a POST request to the endpoint /efficient-hunter-kazuma


response = requests.post('http://127.0.0.1:5000/bugfixer/p2', json=data)# Print the status code
#response = requests.post('https://ubs-yplr.onrender.com/bugfixer/p2', json=data)# Print the status code
print("Status Code:", response.status_code)
print("Content:", response.json())
print("Content:", response.headers.get('Content-Type'))